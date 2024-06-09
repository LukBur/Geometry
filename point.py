import matplotlib.pyplot as plt

class Point(object):

    def __init__(self, x = None, y = None):
        if x is None:
            x = float(input("Współrzędna x: "))
        if y is None:
            y = float(input("Współrzędna y: "))
        self.x = x
        self.y = y

    def show(self):
        print(f"x:{self.x},y:{self.y}")

    def draw(self):
        plt.scatter(self.x, self.y)
        plt.show()