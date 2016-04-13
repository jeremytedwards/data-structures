# coding=utf-8
import random


class Node(object):
    """Create Node class."""

    def __init__(self, val=None):
        """Init Node."""
        self._left = None
        self._right = None
        self._parent = None
        self.data = val

    def in_order(self):
        """Returns the data of all nodes in-order (all left, me, all right)"""
        # Return all the _left items
        if self._left:
            for data in self._left.in_order():
                yield data
        # Return me
        yield self.data
        # Return all the _right
        if self._right:
            for data in self._right.in_order():
                yield data

    def pre_order(self):
        """Returns the data of all nodes in pre-order (me, all left, all right)"""
        # Return me
        yield self.data
        # Return all the _left items
        if self._left:
            for data in self._left.pre_order():
                yield data
        # Return all the _right
        if self._right:
            for data in self._right.pre_order():
                yield data

    def post_order(self):
        """Returns the data of all nodes in post-order (all left, all right, me)"""
        # Return all the _left items
        if self._left:
            for data in self._left.post_order():
                yield data
        # Return all the _right
        if self._right:
            for data in self._right.post_order():
                yield data
        # Return me
        yield self.data

    def breadth_order(self):
        """Returns the data of all nodes in breadth-order (height=0, 1, 2, ...)"""
        visited = []
        to_visit = [self]
        while to_visit:
            node = to_visit.pop(0)
            if node not in visited:
                visited.append(node)
                yield node.data
                if node._left:
                    to_visit.append(node._left)
                if node._right:
                    to_visit.append(node._right)

    def count_node(self):
        """Returns a total count of the left and right children of a node"""
        if self._left:
            left_count = self._left.count_node()
        else:
            left_count = 0
        if self._right:
            right_count = self._right.count_node()
        else:
            right_count = 0
        return left_count + right_count + 1

    def depth_count(self):
        """Returns a total count of the left and right children of a node"""
        if self._left:
            left_depth = self._left.depth_count()
        else:
            left_depth = 0
        if self._right:
            right_depth = self._right.depth_count()
        else:
            right_depth = 0
        return max(left_depth, right_depth) + 1

    def _find_node(self, value):
        """ returns a node with the given value."""
        if self.data == value:
            return self
        elif self.data > value:
            if self._left is None:
                return None
            return self._left._find_node(value)
        else:
            if self._right is None:
                return None
            return self._right._find_node(value)

    def _shift_up_right_del(self):
        """Shift up right node in a delete."""
        if self._parent._right == self:
            self._parent._right = self._right
        else:
            self._parent._left = self._right
        if self._left:
            self._right._left = self._left

    def _shift_up_left_del(self):
        """Shift up left node in a delete."""
        if self._parent._left == self:
            self._parent._left = self._left
        else:
            self._parent._right = self._left

    def _reset_by_value(self, value):
        """
        For a given node replace the value of with the lowest value from my right tree,
        then delete that value from my right tree.
        """
        # find the lowest value of a tree
        to_find = value
        for item in self._right.in_order():
            to_find = item
            self.data = item
            break
        # find node from the right tree
        node = self._right._find_node(to_find)
        # set that nodes parent to None
        node._parent._left = None

    def _rotate_up_right(self):
        """Shift up right node in a delete."""
        promote = self._right
        self._right = promote._left
        if self._parent:
            self._parent._right = promote
        promote._left = self

    def _rotate_up_left(self):
        """Shift up left node in a delete."""
        promote = self._left
        self._left = promote._right
        if self._parent:
            self._parent._left = promote
        promote._right = self

    def _get_balance_diff(self):
        left_depth = 0
        right_depth = 0

        if self._right:
            right_depth = self._right.depth_count()
        if self._left:
            left_depth = self._left.depth_count()

        depth_diff = right_depth - left_depth
        return depth_diff

    def node_balance(self):
        if self._get_balance_diff() <= -2:
            # right tree is heavy
            if self._right._get_balance_diff() <= -1:
                self._right._rotate_up_right()
            if self._right._get_balance_diff() >= 1:
                self._left._rotate_up_left()
            self._rotate_up_right()
        elif self._get_balance_diff() >= 2:
            # left tree is heavy
            if self._left._get_balance_diff() <= -1:
                self._right._rotate_up_right()
            if self._left._get_balance_diff() >= 1:
                self._left._rotate_up_left()
            self._rotate_up_left()

    def _insert(self, val):
        if val == self.data:
            return
        elif self._left is None or self._right is None:
            if val > self.data:
                new_leaf = Node(val)
                new_leaf._parent = self
                self._right = new_leaf
            elif val < self.data:
                new_leaf = Node(val)
                new_leaf._parent = self
                self._left = new_leaf
        elif val > self.data:
            self._right._insert(val)
            self.node_balance()
        elif val < self.data:
            self._left._insert(val)
            self.node_balance()




    # def _get_dot(self):
    #     """recursively prepare a dot graph entry for this node."""
    #     if self._left is not None:
    #         yield "\t%s -> %s;" % (self.data, self._left.data)
    #         for i in self._left._get_dot():
    #             yield i
    #     elif self._right is not None:
    #         r = random.randint(0, 1e9)
    #         yield "\tnull%s [shape=point];" % r
    #         yield "\t%s -> null%s;" % (self.data, r)
    #     if self._right is not None:
    #         yield "\t%s -> %s;" % (self.data, self._right.data)
    #         for i in self._right._get_dot():
    #             yield i
    #     elif self._left is not None:
    #         r = random.randint(0, 1e9)
    #         yield "\tnull%s [shape=point];" % r
    #         yield "\t%s -> null%s;" % (self.data, r)


class Tree(object):
    """Create Tree class."""
    def __init__(self, *args):
        """Init Tree."""
        self.root = None
        for idx, val in enumerate(args):
            self.insert(val)

    def _gen_tree_from_ord_list(self, ordered_list):
        """Given an ordered list this function will create a tree from those values"""
        if ordered_list:
            half = len(ordered_list) // 2

            # yield the middle item round down
            yield ordered_list[half]

            # yield the middle of the left
            for left in self._gen_tree_from_ord_list(ordered_list[:half]):
                yield left

            # yield the middle of the right
            for right in self._gen_tree_from_ord_list(ordered_list[half+1:]):
                yield right

    def _balance_tree(self):
        """
        Given a tree(self) this function will pull the values out and rebuild a balanced
        tree from those values and replace the tree.
        """
        in_order_tree_list = []
        for item in self.root.in_order():
            in_order_tree_list.append(item)

        temp_tree = Tree()
        for value in self._gen_tree_from_ord_list(in_order_tree_list):
            temp_tree.insert(value)

        self.root = temp_tree.root

    def find_node(self, val):
        """Finds a node by value in a tree."""
        to_find = self.root._find_node(val)
        if to_find is None:
            raise ValueError
        else:
            return to_find

    def delete(self, val):
        """Deletes a node by value in a tree."""

        # deleting a nonexistent val - Raises a ValueError
        try:
            to_delete = self.find_node(val)
        except ValueError:
            raise ValueError

        # If tree is only one node, root, delete root
        if to_delete == self.root and self.size() == 1:
            self.root = None
        elif to_delete == self.root and self.size() > 1:
            # Reset the root node from most left child of right tree
            self.root._reset_by_value(val)

        else:
            # replace with the left most node of right subtree
            if to_delete._left is None and to_delete._right is None:
                """if is leaf."""
                if to_delete._parent._left == to_delete:
                    to_delete._parent._left = None
                else:
                    to_delete._parent._right = None
            elif to_delete._left is not None and to_delete._right is None:
                """if has only left."""
                to_delete._shift_up_left_del()
            else:
                """if has 2 children or if has only right."""
                to_delete._shift_up_right_del()

    def insert(self, val):
        """
        Will insert the value val into the BST. If val is already present,
        it will be ignored.
        """
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            self.root._insert(val)


    # def insert_old(self, val):
    #     """
    #     Will insert the value val into the BST. If val is already present,
    #     it will be ignored.
    #     """
    #     node = Node(val)
    #     if self.root is None:
    #         self.root = node
    #     else:
    #         head = self.root
    #         while head:
    #             if head.data == val:
    #                 break
    #             elif head.data > val:
    #                 if head._left:
    #                     head = head._left
    #                 else:
    #                     head._left = node
    #                     node._parent = head
    #                     head.node_balance()
    #                     break
    #             elif head.data < val:
    #                 if head._right:
    #                     head = head._right
    #                 else:
    #                     head._right = node
    #                     node._parent = head
    #                     head.node_balance()
    #                     break

    def contains(self, val):
        """
        Will return True if val is in the BST, False if not.
        """
        if self.root is None:
            return False
        elif self.root.data == val:
            return True
        else:
            head = self.root
            while head:
                if head.data > val:
                    if head._left:
                        if head._left.data == val:
                            return True
                        else:
                            head = head._left
                    else:
                        return False
                elif head.data < val:
                    if head._right:
                        if head._right.data == val:
                            return True
                        else:
                            head = head._right
                    else:
                        return False

    def size(self):
        """
        Will return the integer size of the BST (equal to the total number of values
        stored in the tree). It will return 0 if the tree is empty.
        """
        if self.root is None:
            return 0
        return self.root.count_node()

    def depth(self):
        """
        Will return an integer representing the total number of levels in the tree.
        If there is one value, the depth should be 1, if two values it will be 2, if
        three values it may be 2 or three, depending, etc.
        """
        if self.root is None:
            return 0
        return self.root.depth_count()

    def balance(self):
        """
        Will return an integer, positive or negative that represents how well balanced
        the tree is. Trees which are higher on the _left than the _right should return a
        positive value, trees which are higher on the _right than the _left should return
        a negative value. An ideally-balanced tree should return 0.
        """
        if self.root.data == 0:
            return 0
        if self.root._left is None:
            if self.root._right is None:
                return 0
            else:
                return 1
        else:
            if self.root._right is None:
                return -1
            else:
                if self.root._left.depth_count() > self.root._right.depth_count():
                    return -1
                elif self.root._left.depth_count() == self.root._right.depth_count():
                    return 0
                else:
                    return 1

    def in_order(self):
        return self.root.in_order()

    def pre_order(self):
        return self.root.pre_order()

    def post_order(self):
        return self.root.post_order()

    def breadth_order(self):
        return self.root.breadth_order()






    # def get_dot(self):
    #     """return the tree with root 'self' as a dot graph for visualization"""
    #     return "digraph G{\n%s}" % ("" if self.root.data is None else (
    #         "\t%s;\n%s\n" % (
    #             self.root.data,
    #             "\n".join(self.root._get_dot())
    #         )
    #     ))
