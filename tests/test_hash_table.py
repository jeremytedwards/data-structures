# coding=utf-8
import pytest

from data_structures.hash_table import HashTable


TEST_SIZE = [
    [None, 1024],
    [0, 1024],
    [1, 1024],
    [1024, 1024],
    [2048, 2048],
]

@pytest.mark.parametrize("size", TEST_SIZE)
def test_hashtable_init(size):
    pass


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

TEST_HASHES = []

@pytest.mark.parametrize("key", TEST_HASHES)
def _hash(key):
    """hashes the key provided(note that this is an internal api)"""
    pass
