from __future__ import annotations

from typing import TYPE_CHECKING

from .concrete_visitor import XMLExportVisitor

if TYPE_CHECKING:
    from .shape_interface import Shape


class Application:
    """
    The client code can run ``Visitor`` operations over any set of elements
    without figuring out their concrete classes. The ``accept`` operation
    directs a call to the appropriate operation in the ``Visitor`` object.
    """

    all_shapes: list[Shape]

    def export(self) -> None:
        export_visitor = XMLExportVisitor()

        for shape in self.all_shapes:
            shape.accept(export_visitor)
