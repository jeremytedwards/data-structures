# coding=utf-8


class Node(object):
    """Create Node class."""

    def __init__(self, val=None):
        """Init Node."""
        self._left = None
        self._right = None
        self.data = val

    def in_order(self):
        # Return all the _left items
        if self._left:
            for item in self._left.in_order():
                yield item
        # Return me
        yield self.data

        # Return all the _right
        if self._right:
            for item in self._right.in_order():
                yield item

    def pre_order(self):
        # Return me
        yield self.data

        # Return all the _left items
        if self._left:
            for item in self._left.in_order():
                yield item

        # Return all the _right
        if self._right:
            for item in self._right.in_order():
                yield item

    def post_order(self):
        # Return all the _left items
        if self._left:
            for item in self._left.in_order():
                yield item

        # Return all the _right
        if self._right:
            for item in self._right.in_order():
                yield item

        # Return me
        yield self.data

    def bredth_order(self):
        pass


    def count_node(self):
        if self.left:
            left_count = self.left.count_node()
        else:
            left_count = 0
        if self.right:
            right_count = self.right.count_node()
        else:
            right_count = 0
        return left_count + right_count + 1

    def depth_count(self):
        if self.left:
            left_depth = self.left.depth_count()
        else:
            left_depth = 0
        if self.right:
            right_depth = self.right.depth_count()
        else:
            right_depth = 0
        return max(left_depth, right_depth) + 1


class Tree(object):
    """Create Tree class."""

    def __init__(self):
        """Init Tree."""
        self.root = None

    def insert(self, val):
        """
        will insert the value val into the BST. If val is already present,
        it will be ignored.
        """
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            head = self.root
            while head:
                if head.data == val:
                    break
                elif head.data > val:
                    if head._left:
                        head = head._left
                    else:
                        head._left = node
                elif head.data < val:
                    if head._right:
                        head = head._right
                    else:
                        head._right = node

    def contains(self, val):
        """
        will return True if val is in the BST, False if not.
        """
        if self.root is None:
            return False
        elif self.root.data == val:
            return True
        else:
            head = self.root
            while head:
                if head.data > val:
                    if head.left:
                        if head.left.data == val:
                            return True
                        else:
                            head = head.left
                    else:
                        return False
                elif head.data < val:
                    if head.right:
                        if head.right.data == val:
                            return True
                        else:
                            head = head.right
                    else:
                        return False

    def size(self):
        """
        will return the integer size of the BST (equal to the total number of values
        stored in the tree). It will return 0 if the tree is empty.
        """
        if self.root is None:
            return 0
        return self.root.count_node()

    def depth(self):
        """
        will return an integer representing the total number of levels in the tree.
        If there is one value, the depth should be 1, if two values it will be 2, if t
        hree values it may be 2 or three, depending, etc.
        """
        if self.root is None:
            return 0
        return self.root.depth_count()

    def balance(self):
        """
        will return an integer, positive or negative that represents how well balanced
        the tree is. Trees which are higher on the _left than the _right should return a
        positive value, trees which are higher on the _right than the _left should return
        a negative value. An ideally-balanced tree should return 0.
        """
        if self.root.data == 0:
            return 0
        if self.root.left is None:
            if self.root.right is None:
                return 0
            else:
                return 1
        else:
            if self.root.right is None:
                return -1
            else:
                if self.root.left.depth_count() > self.root.right.depth_count():
                    return -1
                elif self.root.left.depth_count() == self.root.right.depth_count():
                    return 0
                else:
                    return 1

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.root.data is None else (
            "\t%s;\n%s\n" % (
                self.root.data,
                "\n".join(self.root._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.data, self.left.data)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.data, self.right.data)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)

