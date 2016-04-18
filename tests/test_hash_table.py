# coding=utf-8
import pytest

TEST_SIZE = [
    # ["", 1024],
    [0, 0],
    [1, 1],
    [1024, 1024],
    [2048, 2048],
]


@pytest.mark.parametrize("size, result", TEST_SIZE)
def test_hashtable_init(size, result):
    from data_structures.hash_table import HashTable
    test_hash_table = HashTable(size)
    assert len(test_hash_table._storage) == result

def test_hashtable_init_empty():
    from data_structures.hash_table import HashTable
    test_hash_table = HashTable()
    assert len(test_hash_table._storage) == 1024

TEST_KEYS = []


@pytest.mark.parametrize("key", TEST_KEYS)
def get(key):
    """tests the value returned of given key"""
    pass

TEST_KEY_VALUES = []


@pytest.mark.parametrize("key, value", TEST_KEY_VALUES)
def set(key, val):
    """tests insert of a given key, value"""
    pass

TEST_HASHES = [
    ["the", 321],
    ["abcdefghijklmnopqrstuvwxyz", 799],
    [0, 48],
    [1234567890, 525],
]


@pytest.mark.parametrize("key, result", TEST_HASHES)
def test_hash(key, result):
    """hashes the key provided(note that this is an internal api)"""
    from data_structures.hash_table import HashTable
    test_hash_1024 = HashTable()
    # print(test_hash_1024._hash(key))
    assert test_hash_1024._hash(key) == result
