import matplotlib.pyplot as plt
from line import Line
from point import Point

class Polygon:
    
    n = 0  ## liczba wierzchołków
    W = [] ## wierzchołki

    def __init__(self, n):
        self.n = n
        for _ in range(n):
            point = Point()
            self.W.append([point.x, point.y])

    def draw_polygon(self):
        W = self.W
        n = self.n
        for i in range(n):
            print(f"x{i}: {W[i][0]} y{i}: {W[i][1]}")
        
        for i in range(n-1):
            plt.plot([W[i][0],W[i+1][0]], [W[i][1], W[i+1][1]])
        plt.plot([W[n-1][0], W[0][0]], [W[n-1][1], W[0][1]])
        plt.show()

    def point_in_polygon(self, point):
        x = point.x
        y = point.y
        n = self.n
        W = self.W
        intersections = 0
        for i in range(n):
            x1, y1 = W[i]
            x2, y2 = W[(i + 1) % n]
            if ((y1 <= y and y < y2) or (y2 <= y and y < y1)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
                intersections += 1
        if(intersections % 2 != 0):
            print(f"Punkt należy do wielokąta {intersections}")
        else:
            print(f"Punkt nie należy do wielokąta {intersections}")
