import random

class RangeTree1D:

    coords = []

    class Node:
        def __init__(self, point):
            self.point = point
            self.left = None
            self.right = None
    
    def gen_points2D(self):

        x, y = [random.randint(1,100) for _ in range(20)], [random.randint(1,100) for _ in range(20)]
        self.x = x
        self.y = y
        for i in range(len(x)):
            self.coords.append([x[i],y[i]])
        print(self.coords)

o = RangeTree1D
RangeTree1D.gen_points(o)