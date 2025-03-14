from src.rectangle import Rectagle


class Square(Rectagle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Сторона квадрата должна быть положительным числом.")
        super().__init__(side_a, side_a)
