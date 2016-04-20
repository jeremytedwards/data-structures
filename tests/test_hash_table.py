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
    test_hash_table = HashTable(hash_size=0)
    assert len(test_hash_table._storage) == 0


TEST_KEYS = [
    ["key", "the"],
    ["lock", "abc"],
    ["bad", "word"],
]


@pytest.mark.parametrize("key, value", TEST_KEYS)
def test_get(key, value):
    """tests the value returned of given key"""
    from data_structures.hash_table import HashTable
    test_ht = HashTable(hash_size=5)
    test_ht.set("key", "the")
    # print(test_ht._storage[0])
    test_ht.set("lock", "abc")
    test_ht.set("bad", "word")
    assert test_ht.get(key) == value


# TEST_KEY_VALUES = [
#     ["key", "the"],
#     ["lock", "abc"],
#     ["bad", "word"],
# ]


# @pytest.mark.parametrize("key, value", TEST_KEY_VALUES)
def test_set():
    """tests insert of a given key, value"""
    from data_structures.hash_table import HashTable
    test_ht = HashTable(hash_size=5)
    # Test simple insert
    test_ht.set("key", "the")
    assert test_ht.get("key") == "the"

    # Test overwrite when insert same key
    test_ht.set("key", "overwrite")
    assert test_ht.get('key') == "overwrite"


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
