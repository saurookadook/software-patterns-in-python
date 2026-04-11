from __future__ import annotations

from abc import ABC, abstractmethod


class Graphic(ABC):
    """
    The **Component** interface declares common operations for both
    simple and complex objects of a composition.
    """

    @abstractmethod
    def move(self, x: float, y: float) -> None: ...

    @abstractmethod
    def draw(self) -> None: ...
