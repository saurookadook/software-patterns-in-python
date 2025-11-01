from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value):
        self.value = value


class LinkedListNode(Node):
    def __init__(self, value):
        super().__init__(value)

        self.next = None


class BSTNode(Node):
    def __init__(self, value: int):
        super().__init__(value)

        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BSTNode_WithRootRef(Node):
    def __init__(
        self,
        value: int,
        root: Optional[BSTNode_WithRootRef] = None,
    ):
        super().__init__(value)

        self.left: Optional[BSTNode_WithRootRef] = None
        self.right: Optional[BSTNode_WithRootRef] = None
        self.root = root if root is not None else None
