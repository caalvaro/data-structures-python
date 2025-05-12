import pytest
from ..src.binary_tree import BinaryTree


@pytest.fixture
def binary_tree():
    return BinaryTree()


def test_insert(binary_tree):
    binary_tree.insert(1)

    assert binary_tree.root is not None
    assert binary_tree.root.value == 1

    binary_tree.insert(5)

    assert binary_tree.root.right is not None
    assert binary_tree.root.right.value == 5

    binary_tree.insert(3)
    node_five = binary_tree.root.right

    assert node_five.left is not None
    assert node_five.left.value == 3

    binary_tree.insert(6)

    assert node_five.right is not None
    assert node_five.right.value == 6

    binary_tree.insert(-5)

    assert binary_tree.root.left is not None
    assert binary_tree.root.left.value == -5


def test_size(binary_tree):
    binary_tree.insert(1)
    binary_tree.insert(2)

    assert len(binary_tree) == 2

    # binary_tree.remove(1)
    # binary_tree.remove(2)

    # assert len(binary_tree) == 0


def test_contains(binary_tree):
    binary_tree.insert(1)
    binary_tree.insert(2)

    assert 1 in binary_tree
    assert 2 in binary_tree
    assert 3 not in binary_tree

    # binary_tree.remove(2)

    # assert 2 not in binary_tree


def test_inorder(binary_tree):
    binary_tree.insert(1)
    assert binary_tree.inorder() == [1]

    binary_tree.insert(2)
    assert binary_tree.inorder() == [1, 2]

    binary_tree.insert(4)
    assert binary_tree.inorder() == [1, 2, 4]

    binary_tree.insert(-1)
    assert binary_tree.inorder() == [-1, 1, 2, 4]

    binary_tree.insert(-5)
    assert binary_tree.inorder() == [-5, -1, 1, 2, 4]


# def test_remove(binary_tree):
#     with pytest.raises(Exception):
#         binary_tree.remove(1)


# def test_string_set(binary_tree):
#     assert str(binary_tree) == "{}"

#     binary_tree.add(1)

#     assert str(binary_tree) == "{1}"

#     binary_tree.add(2)
#     binary_tree.add(3)

#     assert str(binary_tree) == "{1, 2, 3}"
