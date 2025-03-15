import math
from src.figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус круга должен быть положительным числом.")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
