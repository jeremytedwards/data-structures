#coding=utf-8

import pytest

import __future__


TRIE_TABLE = [
    ("baa", {"b": {"a": {"a": {"$": "$"}}}}),
    ("bat", {'b': {'a': {'t': {'$': '$'}}}}),
    ("ball", {'b': {'a': {'l': {'l': {'$': '$'}}}}}),

]


@pytest.mark.parametrize("test, result", TRIE_TABLE)
def test_insert(test, result):
    from data_structures.trie import Trie
    test_trie = Trie()
    assert test_trie.insert(test) == result


CONTAINS_TABLE = [
    ("ba", False),
    ("batle", False),
    ("ballet", True),
]


@pytest.mark.parametrize("test, result", CONTAINS_TABLE)
def test_contains(test, result):
    from data_structures.trie import Trie
    test_trie = Trie()
    test_trie.insert("ballet")
    assert test_trie.contains(test) == result
