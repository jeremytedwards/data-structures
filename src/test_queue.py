# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import range

import pytest


@pytest.mark.parametrize("params", [
    (),
    ([1],),
    ([1, 2, 3, 4],),
    ("abc",),
])
def test_init(params):
    from queue import Queue
    Queue(*params)


@pytest.mark.parametrize("params", [
    (1,),
    (1, 2),
    ([1, 2], 3, 4),
])
def test_bad_init(params):
    from queue import Queue
    with pytest.raises(TypeError):
        Queue(*params)


LISTS = [
    [],
    [1, 1, 1],
    list(range(10)),
    [[1, 2], [2, 3, 4]],
]


@pytest.mark.parametrize("items", LISTS)
def test_enqueue(items):
    from queue import Queue
    q = Queue()
    for item in items:
        q.enqueue(item)
    for item in items:
        assert q.dequeue() == item


@pytest.mark.parametrize("items", LISTS)
def test_dequeue(items):
    from queue import Queue
    q = Queue(items)
    for item in items:
        assert q.dequeue() == item
    with pytest.raises(IndexError):
        q.dequeue()


def test_peek():
    from queue import Queue
    q = Queue(range(4))
    for _ in range(4):
        assert q.peek() == q.dequeue()
    # queue is now empty
    assert q.peek() is None


def test_size():
    from queue import Queue
    q = Queue(range(4))
    for expected in range(4, 0, -1):
        assert q.size() == expected
        q.dequeue()
    # queue is now empty
    assert q.size() == 0
