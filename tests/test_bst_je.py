# # coding=utf-8
#
# import pytest
#
# from data_structures.bst_je import Tree
#
#
# CONSTRUCTOR_LISTS = [
#     1,
#     5,
#     7,
# ]
#
#
# @pytest.mark.parametrize('val', CONSTRUCTOR_LISTS)
# def test_insert(val):
#     '''
#     will insert the value val into the BST. If val is already present,
#     it will be ignored.
#     '''
#     # Test that the value was inserted
#     tree = Tree([1, 2, 3])
#     tree.insert(val)
#     assert tree.root.data == val
#     print(tree.get_dot())
#
#
#
# CONTAINS_LIST = [
#     [],
# ]
#
#
# @pytest.mark.parametrize('val', CONTAINS_LIST)
# def contains(val):
#     '''
#     will return True if val is in the BST, False if not.
#     '''
#     pass
#
#
# def size():
#     '''
#     will return the integer size of the BST (equal to the total number of values
#     stored in the tree). It will return 0 if the tree is empty.
#     '''
#     pass
#
#
# def depth():
#     '''
#     will return an integer representing the total number of levels in the tree.
#     If there is one value, the depth should be 1, if two values it will be 2, if t
#     hree values it may be 2 or three, depending, etc.
#     '''
#     pass
#
#
# def balance():
#     '''
#     will return an integer, positive or negative that represents how well balanced
#     the tree is. Trees which are higher on the _left than the _right should return a
#     positive value, trees which are higher on the _right than the _left should return
#     a negative value. An ideally-balanced tree should return 0.
#     '''
#     pass