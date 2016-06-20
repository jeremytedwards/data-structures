# coding=utf-8
from __future__ import unicode_literals, print_function
from data_structures.queue_array import ArrayQueue

import pytest


@pytest.mark.parametrize("params", [
    0,
    1,
    8,
    16,
])
def test_init(params):
    aq = ArrayQueue(params)


@pytest.mark.parametrize("params", [
    "abc",
    None,
])
def test_bad_init(params):
    with pytest.raises(TypeError):
        ArrayQueue(*params)


def test_size_empty():
    aq = ArrayQueue(4)
    assert aq.size() == 0

    # confirm size after an enqueue/dequeue
    aq.enqueue(42)
    item = aq.dequeue()
    assert aq.size() == 0


# TODO: @pytest.mark.parametrize() many sizes and check results
# def test_size_full():
#     aq = ArrayQueue(4)
#     assert aq.size() == 0
#
#     # add elements check size
#     for expected in range(4):
#         assert aq.size() == expected
#         aq.dequeue()

@pytest.mark.parametrize("params", [
    [1],                    # one item
    [2, 4, 6],              # more than one
    [2, 4, 6, 8],           # equal to size, full
    [8, 6, 7, 5, 3, 0, 9]   # more than full
])
def test_enqueue(params):
    aq = ArrayQueue(4)
    for item in params:
        aq.enqueue(item)

    assert aq.size() == len(params)


