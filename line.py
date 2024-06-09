import matplotlib.pyplot as plt
from point import Point
from math import sqrt
from numpy import arccos
import math

class Line(object):

    def __init__(self, x1, x2, y1, y2):
        
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        self.u1 = x2-x1
        self.u2 = y2-y1

        if self.x1 == self.x2:
            self.a = 0
            self.b = y1
        else:
            self.a = (self.y1 - self.y2) / (self.x1 - self.x2)
            self.b = self.y1 - self.a * self.x1

    def draw_line(self, x1=0, x2=0):
        if x1 == 0:
            x1 = self.x1
        if x2 == 0:
            x2 = self.x2
        
        plt.plot([x1, x2], [self.y1, self.y2], color='red', label=f"f(x) = {self.a}*x + {self.b}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

    def point_on_line(self, x0 = None, y0 = None):
        
        if(x0 == None and y0 == None):
            print("Dla jakiego punktu x0 sprawdzic przynaleznosc do prostej? ")
            x0 = input()
            y0 = input()

        plt.scatter(x0,y0)
        plt.text(x0,y0,'x0')

        D = abs(self.a * x0 - y0 + self.b) / sqrt(pow(self.a, 2) + 1)
        if D:
            print(f"Punkt nie nalezy do prostej, a jego odlegosc to: {D}")
            plt.plot(label=f"Odleglosc punktu od prostej: {D}")
            self.draw_line()
            return False
        else:
            print("Punkt nalezy do prostej")
            self.draw_line()
            return True
        
    def point_on_segment(self):
        x0 = float(input("Podaj x0 punktu: "))
        y0 = float(input("Podaj y0 punktu: "))
        if self.point_on_line(x0, y0):
            if min(self.x1, self.x2) <= x0 <= max(self.x1, self.x2) and min(self.y1, self.y2) <= y0 <= max(self.y1, self.y2):
                print("\n")
                print("Punkt nalezy do linii")
        else:
            print("Punkt nie nalezy do linii")
        
    def left_right(self, x0, y0):
        left = False
        right = True
        
        if x0 * self.a + self.b == y0:
            print("Punkt p leży na prostej")
            side = 1
        else:
            if self.a < 0:
                if x0 * self.a + self.b < y0:
                    print("Punkt leży na prawo od prostej")
                    side = right
                else:
                    print("Punkt leży na lewo od prostej")
                    side = left
            elif self.a > 0:
                if x0 * self.a + self.b < y0:
                    print("Punkt leży na lewo od prostej")
                    side = left
                else:
                    print("Punkt leży na prawo od prostej")
                    side = right
        
        '''plt.scatter(x0,y0,c="red",label="p")
        self.pokaz_linie(self.x1, self.x2)
        plt.show()'''
        return side

    def translate(self):
        vector_x = float(input("Podaj x wektora: "))
        vector_y = float(input("Podaj y wektora: "))

        plt.plot([self.x1, self.x2], [self.y1, self.y2], color='green', label=f"f(x) = {self.a}*x + {self.b}")
        plt.legend()
        plt.grid(True)

        self.x1 += vector_x
        self.x2 += vector_x
        self.y1 += vector_y
        self.y2 += vector_y
        self.a = (self.y1 - self.y2) / (self.x1 - self.x2)
        self.b = self.y1 - self.a * self.x1

    def reflect_point(self):
        x0 = float(input("x0 punktu: "))
        y0 = float(input("y0 punktu: "))

        plt.scatter(x0, y0, label="original")

        if(self.a != 0):
            x1 = (y0-self.b)/self.a
            y1 = self.a*x0+self.b
            plt.scatter(x1, y1, label="odbity", c="black")
            self.draw_line()
        elif(y0 > self.b):
            y0 -= 2*abs(self.a * x0 - y0 + self.b) / sqrt(pow(self.a, 2) + 1)
            plt.scatter(x0, y0, label="odbity", c="black")
            self.draw_line()
        else:
            y0 += 2*abs(self.a * x0 - y0 + self.b) / sqrt(pow(self.a, 2) + 1)
            plt.scatter(x0, y0, label="odbity", c="black")
            self.draw_line()

    def intersection_point(self, x1 = 0, x2 = 0, y1 = 0, y2 = 0):
        
        if(x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0):
            x1 = float(input("Podaj x1 punktu 1: "))
            y1 = float(input("Podaj y1 punktu 1: "))
            x2 = float(input("Podaj x2 punktu 2: "))
            y2 = float(input("Podaj y2 punktu 2: "))
        
        line = Line(x1, x2, y1, y2)

        if(line.a == self.a):
            if(line.b == self.b):
                print("linie należą do tych samych prostych")
                return True
            else:
                print("proste nigdy się nie przetną")
                return False
        else:
            wsp_x = (line.b - self.b)/(self.a - line.a)
            wsp_y = line.a*wsp_x + line.b
            print(f"Proste przecinaja sie w punkcie x: {wsp_x} i y: {wsp_y}")
            return True

    def dot(vA, vB):
        return vA[0]*vB[0] + vA[1]*vB[1]

    def ang(self, line1):
        # Get nicer vector form
        vA = [(self.x1 - self.x2), (self.y1 - self.y2)]
        vB = [(line1.x1 - line1.x2), (line1.y1 - line1.y2)]

        # Get dot product
        dot_prod = Line.dot(vA, vB)

        # Get magnitudes
        magA = Line.dot(vA, vA) ** 0.5
        magB = Line.dot(vB, vB) ** 0.5

        # Check if either magnitude is zero
        if magA == 0 or magB == 0:
            return 0

        # Get cosine value
        cos_ = dot_prod / (magA * magB)

        # Ensure cos_ is within [-1, 1] range
        cos_ = max(min(cos_, 1.0), -1.0)

        # Get angle in radians and then convert to degrees
        angle_rad = math.acos(cos_)
        angle_deg = math.degrees(angle_rad)
        
        print("Kąt między odcinkami wynosi:", angle_deg,"°")
        return angle_deg

    def calculate_angle(self, line1):
        u1v1 = self.u1 * line1.u1 + self.u2 * line1.u2
        u = math.sqrt(self.u1 ** 2 + self.u2 ** 2)
        v = math.sqrt(line1.u1 ** 2 + line1.u2 ** 2)
        
        if u == 0 or v == 0:
            return 0
        
        cos_alfa = max(min(u1v1 / (u * v), 1.0), -1.0)

        if cos_alfa < -1.0:
            cos_alfa = -1.0
        elif cos_alfa > 1.0:
            cos_alfa = 1.0

        alfa_rad = math.acos(cos_alfa)
        alfa = math.degrees(alfa_rad)
        
        ##print("Kąt między odcinkami wynosi:", alfa,"°")
        return alfa
    
    '''def angle_between_lines(self, line):
        m1 = self.a
        m2 = line.a
        angle_radians = math.atan((m1 - m2) / (1 + m1 * m2))
        angle_degrees = math.degrees(angle_radians)
        print("Kąt między odcinkami wynosi:", angle_degrees,"°")
        return angle_degrees'''