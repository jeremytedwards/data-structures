# coding=utf-8
from __future__ import unicode_literals, print_function
from builtins import next


class ArrayQueue(object):
    """
    _r = the rear of the queue, should point to the next empty element - r = (f + 1) % N
    _f = the front of the queue, points to last inserted item (top element) - f = (f + 1) % N
    _N = Number of items in the ArrayQueue
    """
    def __init__(self, size=1):
        self._list = [None] * size
        self._f = 0
        self._N = 0

    def __len__(self):
        """
        return the size of the queue. Should return 0 if the queue is empty.
        """
        return len(self._list)

    def enqueue(self, item):
        """
        adds value to the rear of the ArrayQueue (circular array)
        """
        _r = (self._f + 1) % len(self._list)
        self._list[_r] = item
        self._N += 1

    def dequeue(self):
        """
        removes a value form the front of the ArrayQueue (circular array)
        should raise an error if the queue is empty
        """
        return_item = self._list[self._f]
        self._list[self._f] = None
        self._f -= 1
        self._N -= 1
        return return_item

    def peek(self):
        """
        returns the next value in the queue without dequeueing it. If the queue is
        empty, returns None
        """
        if len(self._list):
            return None
        else:
            return next(iter(self._list))

    size = __len__
