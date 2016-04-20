# coding=utf-8


class HashTable(object):
    def __init__(self, hash_size=1024):
        self._size = hash_size
        self._storage = [[] for i in range(hash_size)]

    def get(self, key):
        """returns the value stored with the given key"""
        bucket = self._storage[self._hash(key)]
        for item in bucket:
            if item[0] == key:
                # if the item is already in the bucket do nothing
                return item[1]

    def set(self, key, val):
        """stores the given val using the given key"""
        # import pdb;pdb.set_trace()
        bucket = self._storage[self._hash(key)]
        key_found = False
        for index, (t_key, t_val) in enumerate(bucket):
            if key == t_key:
            # if the key is already in the bucket update
                self._storage[self._hash(key)][index] = (key, val)
                key_found = True
                break
        if key_found is False:
            self._storage[self._hash(key)].append((key, val))

    def _hash(self, key):
        """
        hashes the key provided(note that this is an internal api)
        this method prefers a string or integer.
        """
        return sum([ord(c) for c in str(key)]) % self._size
