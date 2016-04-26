# coding=utf-8

from data_structures.bst import Tree
import pytest


def test_insert():
    """Test insert."""
    # Test that the value was inserted
    tree = Tree()
    tree.insert(2)
    assert tree.root.data == 2

    # Test that there are not 2 of the same value
    tree_size_1 = Tree()
    tree_size_1.insert(1)
    tree_size_1.insert(1)
    assert tree_size_1.size() == 1

    tree_1 = Tree(5, 3, 7, 1, 4, 6, 8, 2, 9)
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_1 = []
    for item in tree_1.in_order():
        list_1.append(item)
    assert list_1 == result

    tree_2 = Tree(5, 7, 3, 8, 6, 4, 1, 9, 2)
    list_2 = []
    for item in tree_2.in_order():
        list_2.append(item)
    assert list_2 == result

    # Test inserted node's parent
    tree_3 = Tree(5, 7, 3, 8, 6)
    tree_3.insert(4)
    node = tree_3.find_node(4)
    assert node._parent.data == 3

# TODO: fix this test
# def test_contains():
#     """Test contains."""
#     tree = Tree(2, 3, 4, 5)
#     # will return True if val is in the BST, False if not.
#     assert tree.contains(4) == True
#     assert tree.contains(8) == False

# TODO: fix this test
# def test_size():
#     """Test size."""
#     # Returns 0 when empty
#     tree = Tree()
#     assert tree.size() == 0
#
#     # Returns size when there is size
#     tree = Tree(2, 3, 4, 5, 8)
#     assert tree.size() == 5

def test_depth():
    """Test depth."""
    # Test depth of 0
    tree = Tree()
    assert tree.depth() == 0

    # Test depth of 2
    tree = Tree(5, 3, 6)
    assert tree.depth() == 2

    # Test depth of 3
    tree = Tree(5, 3, 6, 8, 4)
    assert tree.depth() == 3

# TODO: fix this test
# def test_balance():
#     """Test balance."""
#     # An ideally-balanced tree should return 0.
#     tree = Tree(5, 3, 6, 8, 4)
#     assert tree.balance() == 0
#
#     # Trees which are higher on the _left than the _right should return a positive value
#     tree = Tree(5, 3, 6, 8, 4, 9)
#     assert tree.balance() == 1
#
#     # Trees which are higher on the _right than the _left should return a negative value
#     tree = Tree(5, 3, 6, 8, 4, 9, 2, 1, 0)
#     assert tree.balance() == -1


def test_in_order():
    """Test in order."""
    tree_val = [5, 3, 7, 1, 4, 6, 8, 2, 9]
    tree = Tree(*tree_val)
    result = []
    for each in tree.in_order():
        result.append(each)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree_val_unordered = [5, 7, 3, 8, 6, 4, 1, 9, 2]
    tree_2 = Tree(*tree_val_unordered)
    result_2 = []
    for each in tree_2.in_order():
        result_2.append(each)
    assert result_2 == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_pre_order():
    """Test pre order."""
    tree_val = [5, 3, 7, 1, 4, 6, 8, 2, 9]
    tree = Tree(*tree_val)
    result = []
    for each in tree.pre_order():
        result.append(each)
    assert result == [5, 3, 1, 2, 4, 7, 6, 8, 9]
    tree_val_unordered = [5, 7, 3, 8, 6, 4, 1, 9, 2]
    tree_2 = Tree(*tree_val_unordered)
    result_2 = []
    for each in tree_2.pre_order():
        result_2.append(each)
    assert result_2 == [5, 3, 1, 2, 4, 7, 6, 8, 9]


def test_post_order():
    """Test post order."""
    tree_val = [5, 3, 7, 1, 4, 6, 8, 2, 9]
    tree = Tree(*tree_val)
    result = []
    for each in tree.post_order():
        result.append(each)
    assert result == [2, 1, 4, 3, 6, 9, 8, 7, 5]
    tree_val_unordered = [5, 7, 3, 8, 6, 4, 1, 9, 2]
    tree_2 = Tree(*tree_val_unordered)
    result_2 = []
    for each in tree_2.post_order():
        result_2.append(each)
    assert result_2 == [2, 1, 4, 3, 6, 9, 8, 7, 5]


def test_breadth_order():
    """Test breath order."""
    tree_val = [5, 3, 7, 1, 4, 6, 8, 2, 9]
    tree = Tree(*tree_val)
    result = []
    for each in tree.breadth_order():
        result.append(each)
    assert result == tree_val

    # tree_val_unordered = [5, 7, 3, 8, 6, 4, 1, 9, 2]
    # tree_2 = Tree(*tree_val_unordered)
    # result_2 = []
    # for each in tree_2.breadth_order():
    #     result_2.append(each)
    # assert result_2 == tree_val


# TODO: fix this test
# def test_breadth_order_2():
#     """Test breath order."""
#     tree_val = [18, 8, 30, 6, 10, 40, 1, 7, 9, 15, 13]
#     tree = Tree(*tree_val)
#     result = []
#     for each in tree.breadth_order():
#         result.append(each)
#     assert result == tree_val


def test__gen_tree_from_ord_list():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = Tree(*test_list)

    result = []
    result_true = [6, 3, 2, 1, 5, 4, 9, 8, 7, 10]

    for item in tree._gen_tree_from_ord_list(test_list):
        result.append(item)
    assert result_true == result


# def test__balance_tree():
#     test_tree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     tree = Tree(*test_tree)

#     result = []
#     result_true = [6, 3, 2, 1, 5, 4, 9, 8, 7, 10]

#     tree._balance_tree()

#     for item in tree.pre_order():
#         result.append(item)
#     assert result_true == result


def test_find():
    tree = Tree(5, 3, 6, 8, 4, 9)
    result = tree.find_node(3)
    assert result.data == 3

    tree = Tree(5, 3, 6, 8, 4, 9)
    with pytest.raises(ValueError):
        tree.find_node(7)

# TODO: fix this test
# def test_delete():
#     tree = Tree(5, 3, 6, 8, 4, 9, 2, 1, 0)
#     # delete a leaf
#     tree.delete(9)
#     with pytest.raises(ValueError):
#         tree.find_node(9)
#     assert tree.find_node(8)._right == None
#
#     tree = Tree(5, 3, 6, 8, 4, 9, 2, 1, 0)
#     # delete node with only left child
#     tree.delete(1)
#     with pytest.raises(ValueError):
#         tree.find_node(1)
#     assert tree.find_node(2)._left.data == 0
#
#     tree = Tree(5, 3, 6, 8, 4, 9, 2, 1, 0)
#     # delete a node with right or both child
#     tree.delete(3)
#     with pytest.raises(ValueError):
#         tree.find_node(3)
#     assert tree.find_node(5)._left.data == 4
#     assert tree.find_node(4)._left.data == 2
#
#     tree = Tree(5, 3, 6, 8, 4, 9, 2, 1, 0)
#     # delete a nonexistent value
#     with pytest.raises(ValueError):
#         tree.delete(7)
#
#     tree = Tree(10, 8, 12, 6, 11, 13)
#     # delete root node of tree > 1
#     tree.delete(10)
#     with pytest.raises(ValueError):
#         tree.find_node(10)
#     assert tree.root.data == 11
#     assert tree.find_node(12)._left == None
#
#     tree = Tree(10)
#     # delete root of tree == 1
#     tree.delete(10)
#     with pytest.raises(AttributeError):
#         tree.find_node(10)
#     assert tree.root == None


# def test_node_balance():
#     nb_tree = Tree(18, 8, 20, 6, 10, 30, 1, 7, 9, 15)
#     nb_tree.insert(13)
#     result = []
#     for each in nb_tree.breadth_order():
#         result.append(each)
#     expect = [10, 8, 18, 6, 9, 15, 20, 1, 7, 13, 30]
#     assert result == expect
