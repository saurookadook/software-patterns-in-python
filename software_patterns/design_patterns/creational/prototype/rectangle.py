from __future__ import annotations
from typing import Optional

from .shape_prototype import ShapePrototype


class Rectangle(ShapePrototype):
    """Concrete prototype. The cloning method creates a new object \
    in one go by calling the constructor of the current class and \
    passing the current object as the constructor's argument. \
    Performing all the actual copying in the constructor helps to \
    keep the result consistent: the constructor will not return a \
    result until the new object is fully built; thus, no object \
    can have a reference to a partially-built clone.
    """

    height: float | int
    width: float | int

    def __init__(self, source: Optional[Rectangle] = None):
        super().__init__(source)

        if source is not None and isinstance(source, Rectangle):
            self.height = source.height
            self.width = source.width
        else:
            self.height = 0
            self.width = 0

    def clone(self) -> Rectangle:
        return Rectangle(self)

    def get_area(self) -> float | int:
        return self.height * self.width

    def get_perimeter(self) -> float | int:
        return (2 * self.height) + (2 * self.width)
