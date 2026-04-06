from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .visitor_interface import Visitor


class Shape(ABC):
    """
    The element interface declares an ``accept`` method that takes the
    base ``Visitor`` interface as an argument.
    """

    id: str
    x: int
    y: int

    @abstractmethod
    def move(self, x: int, y: int) -> None: ...

    @abstractmethod
    def draw(self) -> None: ...

    @abstractmethod
    def accept(self, v: Visitor) -> None: ...
