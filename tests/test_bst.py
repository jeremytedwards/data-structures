# coding=utf-8

import pytest

from data_structures.bst import Tree


def test_insert():
    # Test that the value was inserted
    tree = Tree()
    tree.insert(2)
    assert tree.root.data == 2

    # TODO: Test that there are not 2 of the same value
    tree.insert(1)
    tree.insert(1)
    assert tree.root.left.data == 1


def test_contains():
    tree = Tree()
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)

    # will return True if val is in the BST, False if not.
    assert tree.contains(4) == True
    assert tree.contains(8) == False


def test_size():
    # Returns 0 when empty
    tree = Tree()
    assert tree.size() == 0

    # Returns size when there is size
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(8)
    assert tree.size() == 5


def test_depth():
    # Test depth of 0
    tree = Tree()
    assert tree.depth() == 0

    # Test depth of 2
    tree.insert(5)
    tree.insert(3)
    tree.insert(6)
    assert tree.depth() == 2

    # Test depth of 3
    tree.insert(8)
    tree.insert(4)
    assert tree.depth() == 3


def test_balance():
    tree = Tree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(6)
    tree.insert(8)
    tree.insert(4)

    # An ideally-balanced tree should return 0.
    assert tree.balance() == 0
    tree.insert(9)

    # Trees which are higher on the left than the right should return a positive value
    assert tree.balance() == 1
    tree.insert(2)
    tree.insert(1)
    tree.insert(0)

    # Trees which are higher on the right than the left should return a negative value
    assert tree.balance() == -1
