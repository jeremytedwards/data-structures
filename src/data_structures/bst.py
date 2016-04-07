# coding=utf-8


class Node(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.data = val

    def _insert_left(self, val):
        node = Node(val)
        self.left = node

    def _insert_left(self, val):
        node = Node(val)
        self.right = node


class Tree(object):
    def __init__(self):
        self.root = Node()


    def insert(self, val):
        """
        will insert the value val into the BST. If val is already present,
        it will be ignored.
        """
        tree = Tree()
        if self.root.data is None:
            self.root.data = val
        else:
            head = self.root
            while head:
                if head.data == val:
                    break
                elif not head.left:
                    head._insert_left(val)
                    break
                elif not head.right:
                    head._insert_right(val)
                    break
                elif head.data > val:
                    head = head.left
                elif head.data < val:
                    head = head.right

    def contains(self, val):
        """
        will return True if val is in the BST, False if not.
        """
        pass

    def size(self):
        """
        will return the integer size of the BST (equal to the total number of values
        stored in the tree). It will return 0 if the tree is empty.
        """
        pass

    def depth(self):
        """
        will return an integer representing the total number of levels in the tree.
        If there is one value, the depth should be 1, if two values it will be 2, if t
        hree values it may be 2 or three, depending, etc.
        """
        pass

    def balance(self):
        """
        will return an integer, positive or negative that represents how well balanced
        the tree is. Trees which are higher on the left than the right should return a
        positive value, trees which are higher on the right than the left should return
        a negative value. An ideally-balanced tree should return 0.
        """
        pass

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

