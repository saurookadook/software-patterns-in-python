import pytest


#### TODO: find out how to fix these imports
# from data_structures.binary_search_tree import BSTOperations
# from data_structures.nodes import BSTNode
from ..binary_search_tree import BSTOperations
from ..nodes import BSTNode


@pytest.fixture
def simple_bst():
    root = BSTNode(6)
    BSTOperations.insert(root, 8)
    BSTOperations.insert(root, 2)
    BSTOperations.insert(root, 5)
    BSTOperations.insert(root, 4)
    BSTOperations.insert(root, 9)
    return root


def test_binary_search_tree():
    root = BSTNode(10)

    assert root.value == 10
    assert root.left is None
    assert root.right is None


def test_binary_search_tree_insertion():
    root = BSTNode(10)
    BSTOperations.insert(root, 8)
    BSTOperations.insert(root, 12)

    assert isinstance(root.left, BSTNode) and root.left.value == 8
    assert isinstance(root.right, BSTNode) and root.right.value == 12


def test_binary_search_tree_search_found(simple_bst):
    result = BSTOperations.search(simple_bst, 9)

    assert isinstance(result, BSTNode) and result.value == 9


def test_binary_search_tree_search_not_found(simple_bst):
    result = BSTOperations.search(simple_bst, 1)

    assert result is None


def test_binary_search_tree_deletion(simple_bst):
    result_in_tree = BSTOperations.search(simple_bst, 5)
    assert isinstance(result_in_tree, BSTNode) and result_in_tree.value == 5

    BSTOperations.delete_node(simple_bst, 5)

    no_result = BSTOperations.search(simple_bst, 5)
    assert no_result is None
