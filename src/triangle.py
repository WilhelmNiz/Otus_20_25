import math
from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны должны быть положительными числами.")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Треугольник с такими сторонами не существует.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
