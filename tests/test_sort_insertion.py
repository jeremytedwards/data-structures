# coding=utf-8
import pytest
from data_structures.sort_insertion import sort_insertion


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
def test_sort_insertion(items, result):
    sorted_list = sort_insertion(items)
    assert sorted_list == result


