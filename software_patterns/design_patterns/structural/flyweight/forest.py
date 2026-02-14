from __future__ import annotations

from typing import Any

from .tree import Tree
from .tree_factory import TreeFactory
from .tree_type import Color, Name, Texture


class Forest:
    """The Tree and the Forest classes are the flyweight's clients. You can
    merge them if you don't plan to develop the Tree class any further.
    """

    trees: list[Tree]

    def plant_tree(
        self, x: int, y: int, name: Name, color: Color, texture: Texture
    ) -> None:
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas: Any) -> None:
        for tree in self.trees:
            tree.draw(canvas)
