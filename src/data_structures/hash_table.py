# coding=utf-8


class HashTable(object):
    def __init__(self, hash_size=1024):
        self._size = hash_size
        self._storage = [[] for i in range(hash_size)]

    def get(self, key):
        """returns the value stored with the given key"""
        bucket = self._storage[self._hash(key)]
        for item in bucket:
            if item == val:
                # if the item is already in the bucket do nothing
                return item


    def set(self, key, val):
        """stores the given val using the given key"""
        bucket = self._storage[self._hash(key)]
        for t_key, t_value in bucket:
            if t_key == key:
                # if the key is already in the bucket update
                self._storage[self._hash(key)][key][val]
                break
            else:
                # if the item is not in the bucket insert as tuple
                self._storage[self._hash(key)].append((key, val))

    def _hash(self, key):
        """
        hashes the key provided(note that this is an internal api)
        this method prefers a string or integer.
        """
        return sum([ord(c) for c in str(key)]) % self._size
