from point import Point
from line import Line
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

class Triangle:
    
    W = [[0, 0], [0, 0], [0, 0]]
    a = 0
    b = 0
    c = 0
    S = 0

    ##dodajmy konstruktor co tworzy trojkat punktami
    '''def __init__(self, a1, a2, a3, b1, b2, b3):
        
        if(a1 != a2 and a2 != a3 and a1 != a3):
            self.W[0][0] = (b1 - b2) / (a2 - a1)
            self.W[0][1] = self.W[0][0] * a1 + b1
            
            self.W[1][0] = (b2 - b3) / (a3 - a2)
            self.W[1][1] = self.W[1][0] * a2 + b2

            self.W[2][0] = (b1 - b3) / (a3 - a1)
            self.W[2][1] = self.W[2][0] * a1 + b1

            x = range(-20, 20)
            y = [a1 * x + b1 for x in x]
            plt.plot(x, y, c='blue')

            x = range(-20, 20)
            y = [a2 * x + b2 for x in x]
            plt.plot(x, y, c='blue')
            
            x = range(-20, 20)
            y = [a3 * x + b3 for x in x]
            plt.plot(x, y, c='blue')
            
            min_x = min(point[0] for point in self.W)
            max_x = max(point[0] for point in self.W)
            min_y = min(point[1] for point in self.W)
            max_y = max(point[1] for point in self.W)

            plt.xlim(min_x - 1, max_x + 1)
            plt.ylim(min_y - 1, max_y + 1)
            self.rysuj_trojkat()
        else: 
            print("Przynajmniej dwie proste są równoległe")'''
    
    def __init__(self, x1, x2, x3, y1, y2, y3):
        
        self.W[0][0] = x1
        self.W[0][1] = y1
        
        self.W[1][0] = x2
        self.W[1][1] = y2

        self.W[2][0] = x3
        self.W[2][1] = y3

        plt.plot(x1, y1, c='blue')

        plt.plot(x2, y2, c='blue')
        
        plt.plot(x3, y3, c='blue')
        
        min_x = min(point[0] for point in self.W)
        max_x = max(point[0] for point in self.W)
        min_y = min(point[1] for point in self.W)
        max_y = max(point[1] for point in self.W)

        plt.xlim(min_x - 1, max_x + 1)
        plt.ylim(min_y - 1, max_y + 1)
        self.draw_triangle()

    def draw_triangle(self):
        x = [point[0] for point in self.W]
        y = [point[1] for point in self.W]

        plt.plot(x, y, c='blue')
        plt.plot([x[0], x[1]], [y[0], y[1]], c='red')
        plt.plot([x[0], x[2]], [y[0], y[2]], c='red')
        plt.plot([x[1], x[2]], [y[1], y[2]], c='red')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()

    def calculate_surface(self):
        self.a = sqrt(pow(self.W[0][0] - self.W[1][0],2) + pow(self.W[0][1] - self.W[1][1],2)) ##p1 p2
        self.b = sqrt(pow(self.W[1][0] - self.W[2][0],2) + pow(self.W[1][1] - self.W[2][1],2)) ##p2 p3
        self.c = sqrt(pow(self.W[0][0] - self.W[2][0],2) + pow(self.W[0][1] - self.W[2][1],2)) ##p1 p3

        p = (self.a + self.b + self.c)/2
        self.S = sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        print("Pole trojkata wynosi: ", self.S)

    def point_in_triangle(self, point):
        x = point.x
        y = point.y
        S = 0

        self.a = sqrt(pow(self.W[0][0] - self.W[1][0], 2) + pow(self.W[0][1] - self.W[1][1], 2))
        self.b = sqrt(pow(self.W[1][0] - self.W[2][0], 2) + pow(self.W[1][1] - self.W[2][1], 2))
        self.c = sqrt(pow(self.W[0][0] - self.W[2][0], 2) + pow(self.W[0][1] - self.W[2][1], 2))
        p = (self.a + self.b + self.c) / 2
        self.S = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        
        a1 = sqrt(pow(x - self.W[0][0], 2) + pow(y - self.W[0][1], 2))
        b1 = self.a
        c1 = sqrt(pow(x - self.W[1][0], 2) + pow(y - self.W[1][1], 2))
        p1 = (a1 + b1 + c1) / 2
        S += sqrt(p1 * (p1 - a1) * (p1 - b1) * (p1 - c1))

        a2 = sqrt(pow(x - self.W[1][0], 2) + pow(y - self.W[1][1], 2))
        b2 = self.b
        c2 = sqrt(pow(x - self.W[2][0], 2) + pow(y - self.W[2][1], 2))
        p2 = (a2 + b2 + c2) / 2
        S += sqrt(p2 * (p2 - a2) * (p2 - b2) * (p2 - c2))

        a3 = sqrt(pow(x - self.W[0][0], 2) + pow(y - self.W[0][1], 2))
        b3 = self.c
        c3 = sqrt(pow(x - self.W[2][0], 2) + pow(y - self.W[2][1], 2))
        p3 = (a3 + b3 + c3) / 2
        S += sqrt(p3 * (p3 - a3) * (p3 - b3) * (p3 - c3))

        if S > self.S:
            print(f"Punkt nie należy do trójkąta (Pole z punktem: {S}), (Pole bez punktu {self.S})")
        else:
            print(f"Punkt należy do trójkąta (Pole z punktem: {S}), (Pole bez punktu {self.S})")

    def p_i_t_angles(self, point):
        alfa_sum = 0
        plt.scatter(point.x, point.y)
        a = [point[0] for point in self.W]
        b = [point[1] for point in self.W]
        
        plt.plot(a, b, c='blue')
        plt.plot([a[0], a[1]], [b[0], b[1]], c='red')
        plt.plot([a[0], a[2]], [b[0], b[2]], c='red')
        plt.plot([a[1], a[2]], [b[1], b[2]], c='red')
        for i in range(3):

            line1 = Line(point.x, self.W[i%3][0], point.y, self.W[i%3][1])
            line2 = Line(point.x, self.W[(i+1)%3][0], point.y, self.W[(i+1)%3][1])
            plt.plot([point.x, self.W[i%3][0]], [point.y, self.W[i%3][1]], '--', color='gray')
            plt.plot([point.x, self.W[(i+1)%3][0]], [point.y, self.W[(i+1)%3][1]], '--', color='gray')
            alfa_sum += line1.calculate_angle(line2)
        if(360 - alfa_sum > 1e-6):
            print("Punkt nie należy do trójkąta")
            plt.show()
        else:
            print("Punkt należy do trójkąta")
            plt.show()