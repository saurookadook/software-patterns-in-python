from __future__ import annotations
from typing import Optional

from .shape_prototype import ShapePrototype


class Rectangle(ShapePrototype):
    def __init__(self, source: Optional[Rectangle] = None):
        super().__init__(source)
