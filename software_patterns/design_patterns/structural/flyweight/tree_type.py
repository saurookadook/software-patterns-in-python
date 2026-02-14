from __future__ import annotations

from dataclasses import dataclass
from typing import Any


Name = str
Color = str
Texture = str


@dataclass
class TreeType:
    """The flyweight class contains a portion of the state of a tree.
    These fields store values that are unique for each particular tree.
    For instance, you won't find the tree's coordinates here, but the
    texture and colors shared between many trees are stored here.
    Since this data is usually BIG, you'd waste a lot of memory by
    keeping it in each tree object. Instead, we can extract texture,
    color, and other repeating data into a separate object which lots of
    individual tree objects can reference.
    """

    name: Name
    color: Color
    texture: Texture

    def draw(self, canvas: Any, x: int, y: int) -> None:
        """
        1. create bitmap of a given type, color, and texture
        2. draw bitmap on canvas at X and Y coords.
        """
        pass
