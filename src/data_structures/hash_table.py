# coding=utf-8


class HashTable(object):
    def __init__(self, hash_size=1024):
        self.size = hash_size

    @staticmethod
    def get(key):
        """returns the value stored with the given key"""
        pass

    @staticmethod
    def set(key, val):
        """stores the given val using the given key"""
        pass

    @staticmethod
    def _hash(key):
        """hashes the key provided(note that this is an internal api)"""
        pass
