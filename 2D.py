import matplotlib.pyplot as plt

class RangeTree2D:
    def __init__(self, points):
        self.root = self.build_tree(points)

    class Node:
        def __init__(self, point):
            self.point = point
            self.left = None
            self.right = None

    def build_tree(self, points, depth=0):
        if not points:
            return None
        dim = depth % 2
        points.sort(key=lambda x: x[dim])
        mid = len(points) // 2
        node = self.Node(points[mid])
        node.left = self.build_tree(points[:mid], depth + 1)
        node.right = self.build_tree(points[mid+1:], depth + 1)
        return node

    def query_range(self, x_min, x_max, y_min, y_max):
        return self._query_range(self.root, x_min, x_max, y_min, y_max, depth=0)

    def _query_range(self, node, x_min, x_max, y_min, y_max, depth):
        if not node:
            return []
        dim = depth % 2
        if node.point[0] < x_min:
            return self._query_range(node.right, x_min, x_max, y_min, y_max, depth + 1)
        elif node.point[0] > x_max:
            return self._query_range(node.left, x_min, x_max, y_min, y_max, depth + 1)
        else:
            if y_min <= node.point[1] <= y_max:
                result = [node.point]
            else:
                result = []
            if dim == 0:
                if node.point[0] >= x_min:
                    result += self._query_range(node.left, x_min, x_max, y_min, y_max, depth + 1)
                if node.point[0] <= x_max:
                    result += self._query_range(node.right, x_min, x_max, y_min, y_max, depth + 1)
            else:
                if node.point[1] >= y_min:
                    result += self._query_range(node.left, x_min, x_max, y_min, y_max, depth + 1)
                if node.point[1] <= y_max:
                    result += self._query_range(node.right, x_min, x_max, y_min, y_max, depth + 1)
            return result


def visualize_points(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y, color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Points Visualization')
    plt.show()


def visualize_query_result(points, query_result):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y, color='blue')
    x_q = [point[0] for point in query_result]
    y_q = [point[1] for point in query_result]
    plt.scatter(x_q, y_q, color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Query Result Visualization')
    plt.show()


# Przykładowe użycie
points_2d = [(2, 3), (5, 7), (8, 1), (9, 4), (3, 6), (6, 9), (1, 2), (7, 5)]
range_tree_2d = RangeTree2D(points_2d)
query_result = range_tree_2d.query_range(3, 7, 2, 8)
print("Punkty w zadanym przedziale:", query_result)

visualize_points(points_2d)
visualize_query_result(points_2d, query_result)
