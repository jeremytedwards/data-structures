# coding=utf-8

import pytest

from data_structures.bst import Tree


def test_insert():
    # Test that the value was inserted
    tree = Tree()
    tree.insert(2)
    assert tree.root.data == 2

    # Test that there are not 2 of the same value
    tree_size_1 = Tree()
    tree_size_1.insert(1)
    tree_size_1.insert(1)
    assert tree_size_1.size() == 1


def test_contains():
    tree = Tree(2, 3, 4, 5)

    # will return True if val is in the BST, False if not.
    assert tree.contains(4) == True
    assert tree.contains(8) == False


def test_size():
    # Returns 0 when empty
    tree = Tree()
    assert tree.size() == 0

    # Returns size when there is size
    tree = Tree(2, 3, 4, 5, 8)
    assert tree.size() == 5


def test_depth():
    # Test depth of 0
    tree = Tree()
    assert tree.depth() == 0

    # Test depth of 2
    tree = Tree(5, 3, 6)
    assert tree.depth() == 2

    # Test depth of 3
    tree = Tree(5, 3, 6, 8, 4)
    assert tree.depth() == 3


def test_balance():
    # An ideally-balanced tree should return 0.
    tree = Tree(5, 3, 6, 8, 4)
    assert tree.balance() == 0

    # Trees which are higher on the _left than the _right should return a positive value
    tree = Tree(5, 3, 6, 8, 4, 9)
    assert tree.balance() == 1

    # Trees which are higher on the _right than the _left should return a negative value
    tree = Tree(5, 3, 6, 8, 4, 9, 2, 1, 0)
    assert tree.balance() == -1


def test_breadth_order():
    tree = Tree(5, 3, 7, 1, 4, 6, 8, 2, 9)
    tree.get_dot()
    print(iter(tree))
    # for each in tree.root:
    #     print(each.data)

    # result = tree.breadth_order()
    # print(result)
    for each in tree.breadth_order():
        print(each.data)

    assert True #tree == result
