from __future__ import annotations
from math import pi
from typing import Optional

from .shape_prototype import ShapePrototype


class Circle(ShapePrototype):
    radius: float | int

    def __init__(self, source: Optional[Circle] = None):
        super().__init__(source)

        if source is not None and isinstance(source, Circle):
            self.radius = source.radius
        else:
            self.radius = 0

    def clone(self) -> Circle:
        return Circle(self)

    def get_area(self) -> float | int:
        return (pi * self.radius) ** 2

    def get_circumference(self) -> float | int:
        return 2 * pi * self.radius

    def get_perimeter(self) -> float | int:
        return self.get_circumference()
