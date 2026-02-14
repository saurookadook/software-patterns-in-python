from __future__ import annotations

from .tree_type import Color, Name, Texture, TreeType


TreeTypeKey = tuple[Name, Color, Texture]


class TreeFactory:
    """Flyweight factory decides whether to re-use an existing flyweight or
    or to create a new object.
    """

    # static field
    tree_types: dict[TreeTypeKey, TreeType] = dict()

    @staticmethod
    def get_tree_type(name: str, color: str, texture: str) -> TreeType:
        maybe_tree_type = TreeFactory.tree_types.get((name, color, texture), None)
        if maybe_tree_type is None:
            maybe_tree_type = TreeType(name, color, texture)
            TreeFactory.tree_types[(name, color, texture)] = maybe_tree_type
        return maybe_tree_type
