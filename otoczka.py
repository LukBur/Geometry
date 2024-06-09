import matplotlib.pyplot as plt
from point import Point
from line import Line
from triangle import Triangle
from polygon import Polygon
import matplotlib as mpl
import math
import cv2

class Otoczka(object):

    points = []
    min_x = 50
    indexOf_min_x = 0
    max_x = 0
    x_start = 0
    y_start = 0
    stack = []

    def __init__(self):
        with open("ksztalt_2.txt", "r") as file:
            n_points = int(file.readline().strip())

            for i in range(n_points):
                x, y = map(int, file.readline().strip().split())
                self.points.append((x, y))
                if self.min_x > x:
                    self.min_x = x
                    self.indexOf_min_x = i
                if self.max_x < x:
                    self.max_x = x
        with open("space_craft1.txt", "r") as file1:
            self.x_start, self.y_start = map(float, file1.readline().strip().split())
            self.vx, self.vy = map(float, file1.readline().strip().split())

    def battlefield(self, duration=2, interval=0.1):
        missile_data = []
        with open("missiles1.txt", "r") as missile_file:
            for line in missile_file:
                missile_data.append(list(map(float, line.strip().split())))

        x_spacecraft = self.x_start
        y_spacecraft = self.y_start

        plt.figure(figsize=(8, 6))


        plt.xlim(0, 1000)
        plt.ylim(0, 1000)

        steps = int(duration / interval)
        vx_per_interval = self.vx * interval
        vy_per_interval = self.vy * interval

        for step in range(steps):
            plt.clf()  

            
            self.graham_scan()

            plt.plot([point[0] for point in self.points], [point[1] for point in self.points], 'bo')

            plt.plot([point[0] for point in self.stack], [point[1] for point in self.stack], 'r-')

            plt.plot(x_spacecraft, y_spacecraft, 'go', label='Spacecraft')

            for missile_time, missile_x, missile_y, missile_vx, missile_vy in missile_data:
                if missile_time <= step * interval:
                    missile_x += missile_vx * (step * interval - missile_time)
                    missile_y += missile_vy * (step * interval - missile_time)
                    plt.plot(missile_x, missile_y, 'rx', label='Missile')

            plt.xlim(0, 1000)
            plt.ylim(0, 1000)

            plt.pause(interval)

        plt.show()


    def jarvis_march(self):
        def direction(p, q, r):
            return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])

        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        index = self.indexOf_min_x
        result = []
        result.append(self.points[index])
        while True:
            q = (index + 1) % len(self.points)
            for i in range(len(self.points)):
                if i == index:
                    continue
                d = direction(self.points[index], self.points[i], self.points[q]) 
                if d > 0 or (d == 0 and distance(self.points[i], self.points[index]) > distance(self.points[q], self.points[index])):
                    q = i
            index = q
            if index == self.indexOf_min_x:
                break
            result.append(self.points[q])

        plt.figure(figsize=(8, 6))
        plt.plot([point[0] for point in self.points], [point[1] for point in self.points], 'bo', label='Points')
        plt.plot([point[0] for point in result], [point[1] for point in result], 'r-', label='Convex Hull')
        plt.grid(True)
        plt.show()

        return result

    def graham_scan(self):
        def cross_product(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

        points = sorted(self.points, key=lambda x: (x[1], x[0]))
        for p in points:
            while len(self.stack) > 1 and cross_product(self.stack[-2], self.stack[-1], p) <= 0:
                self.stack.pop()
            self.stack.append(p)

        points.reverse()
        for p in points:
            while len(self.stack) > 1 and cross_product(self.stack[-2], self.stack[-1], p) <= 0:
                self.stack.pop()
            self.stack.append(p)

        return self.stack

    def draw_polygon(self):
        n = self.n
        for i in range(n):
            print(f"x{i}: {self.W[i][0]} y{i}: {self.W[i][1]}")
        
        for i in range(n-1):
            plt.plot([self.W[i][0], self.W[i+1][0]], [self.W[i][1], self.W[i+1][1]])
        plt.plot([self.W[n-1][0], self.W[0][0]], [self.W[n-1][1], self.W[0][1]])
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
    

o = Otoczka()
o.jarvis_march()

