from __future__ import annotations

from typing import Any, Optional

from software_patterns.data_structures.nodes import BSTNode


class BSTOperations:
    @staticmethod
    def insert(node: BSTNode | None, value: Any) -> BSTNode:
        if node is None:
            return BSTNode(value)

        if node.value < value:
            node.right = BSTOperations.insert(node.right, value)
        else:
            node.left = BSTOperations.insert(node.left, value)

        return node

    @staticmethod
    def search(node: BSTNode | None, value: Any) -> BSTNode | None:
        if node is None or node.value == value:
            return node

        if node.value < value:
            return BSTOperations.search(node.right, value)
        else:
            return BSTOperations.search(node.left, value)

    @staticmethod
    def delete_node(node: BSTNode | None, value: Any) -> BSTNode | None:
        """Deletes and returns the `BSTNode` containing the value `value` from the BST.
        Returns `None` if no `BSTNode` was found for the provided value `value`.
        """
        if node is None:
            return node

        # If value `value` is less than `node`'s value, then it lies in left subtree
        if value < node.value:
            node.left = BSTOperations.delete_node(node.left, value)
        # If value `value` is greater than `node`'s value, then it lies in right subtree
        elif value > node.value:
            node.right = BSTOperations.delete_node(node.right, value)
        # If value `value` is equal to `node`'s value, then this is `Node` to be deleted
        else:
            # If `Node` with only one child or no child,
            # the `node`'s right child replaces `node` if the left child doesn't exist
            if node.left is None:
                temp = node.right
                node = None  # NOTE: I believe this is to help the garbage collector
                return temp
            elif node.right is None:
                temp = node.left
                node = None  # NOTE: I believe this is to help the garbage collector
                return temp

            # If `node` has two children, get the inorder successor
            # (a.k.a., smallest in the right subtree)
            temp = BSTOperations.min_value_node(node.right)
            # Copy the inorder successor's content to this `node`
            node.value = temp.value
            # Delete the inorder successor
            node.right = BSTOperations.delete_node(node.right, temp.value)

        return node

    @staticmethod
    def min_value_node(node: BSTNode):
        """Finds the `Node` with the smallest value in a BST."""
        if not node or not isinstance(node, BSTNode):
            raise ValueError(
                f"Argument 'node' must be an instance of 'BSTNode'. Received: {node} ({type(node)})"
            )

        current = node

        # The smallest value is located at the leftmost leaf.
        # Therefore, we iterate until the left child node is None.
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def traverse_inorder(node: BSTNode | None) -> None:
        if node is not None:
            BSTOperations.traverse_inorder(node.left)
            print(node.value)
            BSTOperations.traverse_inorder(node.right)
