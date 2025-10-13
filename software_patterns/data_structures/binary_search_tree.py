from typing import Optional


class BSTNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BSTNode_WithRootRef:
    def __init__(
        self,
        value: int,
        root: Optional["BSTNode_WithRootRef"] = None,
    ):
        self.value = value
        self.left = None
        self.right = None
        self.root = root if root is not None else None
