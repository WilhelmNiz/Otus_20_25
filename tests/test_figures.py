from src.square import Square
from src.circle import Circle
from src.rectangle import Rectangle
from src.triangle import Triangle
import pytest


@pytest.mark.parametrize("shape_class, sides, expected_exception", [
    (Rectangle, (-1, 3), ValueError),
    (Triangle, (3, -4, 5), ValueError),
    (Triangle, (1, 1, 3), ValueError),
    (Square, (-5,), ValueError),
    (Circle, (-14,), ValueError),
])
def test_creation_with_negative_side(shape_class, sides, expected_exception):
    """
    Проверка создания фигуры с некорректными параметрами.
    Ожидается исключение ValueError.
    """
    with pytest.raises(expected_exception):
        shape_class(*sides)

@pytest.mark.parametrize("shape_class, sides, expected_perimeter", [
    (Rectangle, (1, 3), 8),
    (Rectangle, (1.5, 3.5), 10),
    (Triangle, (5, 5, 6), 16),
    (Triangle, (5.5, 5.5, 6.5), 17.5),
    (Square, (5,), 20),
    (Square, (5.5,), 22),
    (Circle, (14,), 87.96),
    (Circle, (14.5,), 91.10),
])
def test_figure_perimeter(shape_class, sides, expected_perimeter):
    """
    Проверка вычисления периметра фигуры.
    """
    c = shape_class(*sides)
    assert  pytest.approx(c.perimeter, 0.001) == expected_perimeter, "Ответ не соответствует ожидаемому значению"


@pytest.mark.parametrize("shape_class, sides, expected_area", [
    (Rectangle, (2, 4), 8),
    (Rectangle, (2.5, 4.5), 11.25),
    (Triangle, (6, 7, 7), 18.97),
    (Triangle, (6.5, 6.5, 7.5), 19.90),
    (Square, (6,), 36),
    (Square, (6.5,), 42.25),
    (Circle, (15,), 706.85),
    (Circle, (15.5,), 754.76),
])
def test_figure_area(shape_class, sides, expected_area):
    """
    Проверка вычисления площади фигур.
    """
    c = shape_class(*sides)
    expected_area = expected_area
    assert pytest.approx(c.area, 0.001) == expected_area, "Ответ не соответствует ожидаемому значению"

@pytest.mark.parametrize("shape_class, sides, shape_class2, sides2, expected_add_area", [
    (Rectangle, (6, 4), Triangle, (8, 8, 9), 53.76),
    (Triangle, (7, 7, 9), Square, (8,), 88.12),
    (Square, (9,), Circle, (18,), 1098.87)
])
def test_figure_add_area(shape_class, sides, shape_class2, sides2, expected_add_area):
    f1 = shape_class(*sides)
    f2 = shape_class2(*sides2)
    assert pytest.approx(f1.add_area(f2), 0.001) == expected_add_area, "Ответ не соответствует ожидаемому значению"

@pytest.mark.parametrize("invalid_figure", [(1), ("Figure")])
def test_figure_add_area_with_invalid_figure(invalid_figure):
    """
    Проверка, что метод add_area выбрасывает исключение, если переданный объект не является фигурой.
    """
    r = Rectangle(5, 10)
    invalid_figure = invalid_figure
    with pytest.raises(ValueError):
        r.add_area(invalid_figure)
