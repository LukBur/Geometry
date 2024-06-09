import matplotlib.pyplot as plt

class RangeTree1D:
    def __init__(self, points):
        self.root = self.build_tree(points)

    class Node:
        def __init__(self, point):
            self.point = point
            self.left = None
            self.right = None

    def build_tree(self, points):
        if not points:
            return None
        points.sort()
        mid = len(points) // 2
        node = self.Node(points[mid])
        node.left = self.build_tree(points[:mid])
        node.right = self.build_tree(points[mid+1:])
        return node

    def query_range(self, start, end):
        return self._query_range(self.root, start, end)

    def _query_range(self, node, start, end):
        if not node:
            return []
        if node.point < start:
            return self._query_range(node.right, start, end)
        elif node.point > end:
            return self._query_range(node.left, start, end)
        else:
            ##colored = [node.point] + self._query_range(node.left, start, end) + self._query_range(node.right, start, end)
            return [node.point] + self._query_range(node.left, start, end) + self._query_range(node.right, start, end)

    def visualize_tree(self):
        levels = self._get_tree_levels(self.root)
        self._plot_tree(levels, 0, len(levels), 0)

    def _get_tree_levels(self, node):
        if not node:
            return []
        left_levels = self._get_tree_levels(node.left)
        right_levels = self._get_tree_levels(node.right)
        return [(node.point, left_levels, right_levels)] + left_levels + right_levels

    def _plot_tree(self, levels, left, right, depth):
        if left >= right or depth >= len(levels):
            return
        mid = (left + right) // 2
        node, left_levels, right_levels = levels[depth]
        plt.plot([mid, mid], [depth, depth-1], 'k-')
        plt.text(mid, depth, str(node), ha='center', va='center', backgroundcolor='w')
        self._plot_tree(left_levels, left, mid, depth+1)
        self._plot_tree(right_levels, mid+1, right, depth+1)


# Przykładowe użycie
points_1d = [7, 2, 5, 9, 1, 11, 4, 8]
range_tree_1d = RangeTree1D(points_1d)
print(range_tree_1d.query_range(3, 8))  # Wyświetli [4, 5, 7, 8]

# Wizualizacja drzewa
range_tree_1d.visualize_tree()
plt.title('Visualisation of 1D Range Tree')
plt.xlabel('Index')
plt.ylabel('Depth')
plt.show()
