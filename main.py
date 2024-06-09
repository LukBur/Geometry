from point import Point
from line import Line
from triangle import Triangle
from polygon import Polygon
import matplotlib.pyplot as plt
import matplotlib as mpl

point1 = Point()
point2 = Point()
line1 = Line(point1.x, point2.x, point1.y, point2.y)

while True:
    print("\n")
    print("1. Sprawdz czy punkt nalezy do linii")
    print("2. Pokaz linie")
    print("3. Sprawdz po ktorej stronie linii jest punkt")
    print("4. Wykonaj translację linii")
    print("5. Odbij punkt względem linii")
    print("6. Punkt przecięcia z inną prostą")
    print("7. Rysuj trójkąt")
    print("8. Licz pole trójkąta")
    print("9. Dodaj linię")
    print("10. Oblicz kąt między liniami")
    print("11. Sprawdź czy punkt należy do trójkąta")
    print("12. Rysuj wielokąt")
    print("13. Sprawdź czy punkt należy do wielokąta")
    print("14. Opuść program")

    choice = input("Opcja: ")
    plt.grid(True)  # Show grid

    
    if choice == '1':
        line1.point_on_segment()

    elif choice == '2':
        line1.draw_line()

    elif choice == '3':
        line1.left_right()

    elif choice == '4':
        line1.translate()

    elif choice == '5':
        line1.reflect_point()

    elif choice == '6':
        line1.intersection_point()

    elif choice == '7':
        x1 = float(input("Podaj x1: "))
        y1 = float(input("Podaj y1: "))
        x2 = float(input("Podaj x2: "))
        y2 = float(input("Podaj y2: "))
        x3 = float(input("Podaj x3: "))
        y3 = float(input("Podaj y3: "))
        triangle = Triangle(x1, x2, x3, y1, y2, y3)

    elif choice == '8':
        if(triangle):
            triangle.calculate_surface()

    elif choice == '9':
        print("Podawanie końców linii")
        point1 = Point()
        point2 = Point()
        line2 = Line(point1.x, point2.x, point1.y, point2.y)
        plt.plot([point1.x, point2.x], [point1.y, point2.y])

    elif choice == '10':
        Line.ang(line1, line2)

    elif choice == '11':
        point = Point()
        triangle.p_i_t_angles(point)
    
    elif choice == '12':
        polygon = Polygon(8)
        polygon.draw_polygon()

    elif choice == '13':
        point = Point()
        polygon.point_in_polygon(point)

    elif choice == '14':
        print("Program zakończono.")
        break
    elif choice == '15':
        plt.plot([1,2],[2,4])
        plt.plot([2,-1],[4,-1])
        plt.plot([-1,-1],[-1,4])
        plt.show()
    else:
        print("Mozesz wybrac tylko opcje od 1 do 15.")