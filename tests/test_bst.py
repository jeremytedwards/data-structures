# coding=utf-8

import pytest

from data_structures.bst import Tree

CONSTRUCTOR_LISTS = [
    1,
    5,
    7,
]


@pytest.mark.parametrize('val', CONSTRUCTOR_LISTS)
def test_insert(val):
    '''
    will insert the value val into the BST. If val is already present,
    it will be ignored.
    '''
    # Test that the value was inserted
    tree = Tree()
    tree.insert(val)
    assert tree.root.data == val

    # test that there are not 2 of the same value
    tree = Tree()
    tree.insert(2)
    print(tree.get_dot())

    assert tree.root.data == 2



CONTAINS_LIST = [
    [],
]


@pytest.mark.parametrize('val', CONTAINS_LIST)
def contains(val):
    '''
    will return True if val is in the BST, False if not.
    '''
    pass


def size():
    '''
    will return the integer size of the BST (equal to the total number of values
    stored in the tree). It will return 0 if the tree is empty.
    '''
    pass


def depth():
    '''
    will return an integer representing the total number of levels in the tree.
    If there is one value, the depth should be 1, if two values it will be 2, if t
    hree values it may be 2 or three, depending, etc.
    '''
    pass


def balance():
    '''
    will return an integer, positive or negative that represents how well balanced
    the tree is. Trees which are higher on the left than the right should return a
    positive value, trees which are higher on the right than the left should return
    a negative value. An ideally-balanced tree should return 0.
    '''
    pass