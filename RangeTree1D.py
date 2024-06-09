import random
import matplotlib.pyplot as plt

class RangeTree1D:
    coords1D = []
    var = []
    def __init__(self):
        self.root = self.gen_1D_Tree(self.coords1D)

    class Node:
        def __init__(self, point):
            self.point = point
            self.left = None
            self.right = None
    
    @classmethod
    def gen_1D_coords(cls):
        cls.coords1D = [random.randint(1, 100) for _ in range(20)]
        return cls.coords1D

    def gen_1D_Tree(self, coords1D):
        coords1D.sort()
        if not coords1D:
            return None
        median = len(coords1D) // 2
        node = self.Node(coords1D[median])
        node.left = self.gen_1D_Tree(coords1D[:median])
        node.right = self.gen_1D_Tree(coords1D[median+1:])
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
            self.var += [node.point] + self._query_range(node.left, start, end) + self._query_range(node.right, start, end)
            return [node.point] + self._query_range(node.left, start, end) + self._query_range(node.right, start, end)

    def plot_tree(self, start, end):
        plt.figure(figsize=(10, 8))
        self._plot_tree(self.root, 0, 100, 0, start, end)
        plt.title('Range 1D Tree')
        plt.show()

    def _plot_tree(self, node, left, right, depth, start, end):
        if not node:
            return
        mid = (left + right) // 2
        if start <= node.point <= end:
            plt.plot(mid, depth, 'ro') 
        else:
            plt.plot(mid, depth, 'bo') 
        
        if node.left:
            left_mid = (left + mid) // 2
            plt.plot([mid, left_mid], [depth, depth-1], 'k-')  
            self._plot_tree(node.left, left, mid, depth-1, start, end)
        if node.right:
            right_mid = (mid + right) // 2
            plt.plot([mid, right_mid], [depth, depth-1], 'k-') 
            self._plot_tree(node.right, mid, right, depth-1, start, end)

RangeTree1D.gen_1D_coords()
range_tree_1d = RangeTree1D()
print(range_tree_1d.query_range(30, 80)) 
range_tree_1d.plot_tree(30, 80)
