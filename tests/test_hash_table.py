# coding=utf-8
import pytest


@pytest.fixture(scope='session')
def words():
    d = {}
    with open('test_data/words', 'r') as f:
        for word in f:
            word = word.strip()
            if word not in d:
                d[word] = len(d)
    return d


def test_words(words):
    from data_structures.hash_table import HashTable
    test_hash_table = HashTable()
    for k, v in words.items():
        test_hash_table.set(k, v)
    for k, v in words.items():
        assert test_hash_table.get(k) == v


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


def test_hashtable_init_none():
    from data_structures.hash_table import HashTable
    test_hash_table = HashTable(hash_size=10)
    assert test_hash_table.get(5) == None


TEST_KEYS = [
    ["key", "the"],
    ["lock", "abc"],
    ["bad", "word"],
]


@pytest.mark.parametrize("key, value", TEST_KEYS)
def test_get(key, value):
    """tests the value returned of given key"""
    from data_structures.hash_table import HashTable
    test_ht = HashTable(5)
    test_ht.set("key", "the")
    # print(test_ht._storage[0])
    test_ht.set("lock", "abc")
    test_ht.set("bad", "word")
    assert test_ht.get(key) == value


TEST_KEY_VALUES = [
    ["key", "the"],
    ["lock", "abc"],
    ["bad", "word"],
]


@pytest.mark.parametrize("key, value", TEST_KEY_VALUES)
def test_set(key, value):
    """tests insert of a given key, value"""
    from data_structures.hash_table import HashTable
    test_ht = HashTable(5)
    # Test simple insert
    test_ht.set(key, value)
    assert test_ht.get(key) == value

    # Test overwrite when insert same key
    test_ht.set(key, "overwrite")
    assert test_ht.get(key) == "overwrite"


def test_set_typeerror():
    from data_structures.hash_table import HashTable
    test_ht = HashTable(5)
    # Test non-string insert
    with pytest.raises(TypeError):
        test_ht.set(123, "value")


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
