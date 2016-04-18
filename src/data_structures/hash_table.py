# coding=utf-8


class HashTable(object):
    def __init__(self, hash_size=1024):
        self._size = hash_size
        self.storage = [[] for i in range(hash_size)]

    def get(self, key):
        """returns the value stored with the given key"""
        pass

    def set(self, key, val):
        """stores the given val using the given key"""
        pass

    def _hash(self, key):
        """
        hashes the key provided(note that this is an internal api)
        this method prefers a string.
        """
        return sum([ord(c) for c in str(key)]) % self._size
