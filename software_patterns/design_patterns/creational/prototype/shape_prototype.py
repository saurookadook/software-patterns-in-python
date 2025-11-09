from __future__ import annotations

from typing import Optional


class ShapePrototype:

    class NotImplemented(NotImplementedError):
        pass

    color: str
    x: int
    y: int

    def __init__(self, source: Optional[ShapePrototype] = None):
        if source is not None and isinstance(source, ShapePrototype):
            self.color = source.color
            self.x = source.x
            self.y = source.y

    def clone(self) -> ShapePrototype:
        raise ShapePrototype.NotImplemented()

    def get_area(self) -> float | int:
        raise ShapePrototype.NotImplemented()
