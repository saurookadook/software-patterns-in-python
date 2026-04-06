"""
**ConcreteVisitors** implement several versions of the same algorithm, which
can work with all concrete element classes.

You can experience the biggest benefit of the ``Visitor`` pattern when using
it with a complex object structure such as a **Composite Tree**. In this case,
it might be helpful to store some intermediate state of the algorithm while
executing the ``Visitor``'s methods over various objects of the structure.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .visitor_interface import Visitor

if TYPE_CHECKING:
    from .concrete_shapes import Dot, Circle, Rectangle, CompoundShape


class XMLExportVisitor(Visitor):
    def visit_dot(self, d: Dot) -> None:
        """
        Export the dot's ID and center coordinates.
        """

    def visit_circle(self, c: Circle) -> None:
        """
        Export the circle's ID, center coordinates, and radius.
        """

    def visit_rectangle(self, r: Rectangle) -> None:
        """
        Export the rectangle's ID, top-left coordinates, width, and height.
        """

    def visit_compound_shape(self, cs: CompoundShape) -> None:
        """
        Export the shape's ID as well as the list of its children's IDs.
        """
