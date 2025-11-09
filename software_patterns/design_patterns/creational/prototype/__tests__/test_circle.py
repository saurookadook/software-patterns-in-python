import pytest
from math import pi

from ..circle import Circle


@pytest.fixture
def circle():
    c = Circle()
    c.radius = 5
    return c


def test_circle_get_area(circle):
    assert circle.get_area() == (pi * circle.radius) ** 2


def test_circle_get_perimeter(circle):
    assert circle.get_perimeter() == (2 * pi * circle.radius)


def test_circle_should_be_cloneable(circle):
    assert callable(circle.clone) == True

    circle_clone = circle.clone()

    assert isinstance(circle_clone, Circle)
    assert circle_clone is not circle
    assert circle_clone == circle
