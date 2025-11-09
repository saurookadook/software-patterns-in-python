from __future__ import annotations
from typing import Optional

from .shape_prototype import ShapePrototype


class Circle(ShapePrototype):
    def __init__(self, source: Optional[Circle] = None):
        super().__init__(source)
