from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .concrete_shapes import Dot, Circle, Rectangle, CompoundShape


class Visitor(ABC):
    """The ``Visitor`` interface declares a set of visiting methods that
    correspond to element classes. The signature of a visiting method lets
    the visitor identify the exact class of the element that it's dealing with.
    """

    @abstractmethod
    def visit_dot(self, d: Dot) -> None: ...

    @abstractmethod
    def visit_circle(self, c: Circle) -> None: ...

    @abstractmethod
    def visit_rectangle(self, r: Rectangle) -> None: ...

    @abstractmethod
    def visit_compound_shape(self, cs: CompoundShape) -> None: ...
