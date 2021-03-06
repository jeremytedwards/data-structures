# coding=utf-8
import pytest
from data_structures.sort_quick import quicksort


TESTING_LISTS = [
    ([], []),
    ([1], [1]),
    ([1, 1], [1, 1]),
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([20, 40, 30], [20, 30, 40]),
    ([3, 2, 1], [1, 2, 3]),
    ([5, 10, 3, 11, 12, 1, 7], [1, 3, 5, 7, 10, 11, 12]),
    ([10, 100, 12, 3, 8, 19, 33], [3, 8, 10, 12, 19, 33, 100]),
]


@pytest.mark.parametrize('items, result', TESTING_LISTS)
def test_quicksort(items, result):
    sorted_list = quicksort(items)
    assert sorted_list == result