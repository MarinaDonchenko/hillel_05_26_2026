from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side size must be greater than 0")
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius size must be greater than 0")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Trapezoid(Figure):
    def __init__(self, base1, base2, height, side1, side2):
        if base1 <= 0 or base2 <= 0 or height <= 0 or side1 <= 0 or side2 <= 0:
            raise ValueError("Side size must be greater than 0")
        self.__base1 = base1
        self.__base2 = base2
        self.__height = height
        self.__side1 = side1
        self.__side2 = side2

    def area(self):
        return (self.__base1 + self.__base2) / 2 * self.__height

    def perimeter(self):
        return self.__base1 + self.__base2 + self.__side1 + self.__side2


figures = [
        Circle(7),
        Square(6),
        Trapezoid(4, 8, 5, 4, 4)
]

for figure in figures:
    print(f"{figure.__class__.__name__}:")
    print(f"  Area: {figure.area():.2f}")
    print(f"  Perimeter: {figure.perimeter():.2f}")
    print()


