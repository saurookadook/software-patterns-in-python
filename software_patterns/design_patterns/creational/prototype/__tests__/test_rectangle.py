import pytest

from ..rectangle import Rectangle


@pytest.fixture
def rectangle():
    r = Rectangle()
    r.height = 5
    r.width = 10
    return r


def test_rectangle_get_area(rectangle):
    assert rectangle.get_area() == rectangle.height * rectangle.width


def test_rectangle_get_perimeter(rectangle):
    assert rectangle.get_perimeter() == (2 * rectangle.height) + (2 * rectangle.width)


def test_rectangle_should_be_cloneable(rectangle):
    assert callable(rectangle.clone) == True

    rectangle_clone = rectangle.clone()

    assert isinstance(rectangle_clone, Rectangle)
    assert rectangle_clone is not rectangle
    assert rectangle_clone == rectangle
