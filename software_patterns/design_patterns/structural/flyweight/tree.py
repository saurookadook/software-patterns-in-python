from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .tree_type import TreeType


@dataclass
class Tree:
    """The contextual object contains the extrinsic part of the tree state.
    An application can create billions of these since they are pretty small:
    just two integer coordinates and a reference field.
    """

    x: int
    y: int
    type: TreeType

    def draw(self, canvas: Any) -> None:
        self.type.draw(canvas, self.x, self.y)
