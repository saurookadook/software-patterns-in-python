"""
Each concrete element class must implement the ``accept`` method in such
a way that it calls the ``Visitor``'s method that corresponds to the
element's class.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .shape_interface import Shape

if TYPE_CHECKING:
    from .visitor_interface import Visitor


class Dot(Shape):
    def accept(self, v: Visitor) -> None:
        v.visit_dot(self)


class Circle(Shape):
    def accept(self, v: Visitor) -> None:
        v.visit_circle(self)


class Rectangle(Shape):
    def accept(self, v: Visitor) -> None:
        v.visit_rectangle(self)


class CompoundShape(Shape):
    def accept(self, v: Visitor) -> None:
        v.visit_compound_shape(self)
