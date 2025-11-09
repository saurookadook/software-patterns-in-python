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
            for key, value in source.__dict__.items():
                setattr(self, key, value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False

        for key, value in other.__dict__.items():
            if getattr(self, key) != value:
                return False

        return True

    def clone(self) -> ShapePrototype:
        raise ShapePrototype.NotImplemented()

    def get_area(self) -> float | int:
        raise ShapePrototype.NotImplemented()
