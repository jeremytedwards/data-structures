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


def test_traversal():
    from data_structures.trie import Trie
    test_trie = Trie()
    test_trie.insert("a")
    test_trie.insert("apple")
    test_trie.insert("apprentice")
    assert sorted([item for item in test_trie.traversal()]) == ['a', 'apple', 'apprentice']


def test_autocomplete_not_root():
    """Test autocomplete not from root."""
    from data_structures.trie import Trie
    trie = Trie()
    burn = "burn"
    sfkj = "sfkj"
    burneman = "burneman"
    lol = "lol"
    loled = "loled"
    lol_s = "lol's"
    word_list = [burn, sfkj, burneman, lol, loled, lol_s]
    for indx in word_list:
        trie.insert(indx)
    auto = trie.autocomplete('lol')
    assert lol_s in auto
    assert loled in auto
    assert lol in auto
    assert sfkj not in auto


def test_autocomplete_non_existent_token():
    """Test that autocomplete returns empty list if token not in trie."""
    from data_structures.trie import Trie
    trie = Trie()
    token1 = "burn"
    token2 = "sfkj"
    token3 = "burneman"
    trie.insert(token1)
    trie.insert(token2)
    trie.insert(token3)
    auto = trie.autocomplete('goal')
    assert auto == {}

