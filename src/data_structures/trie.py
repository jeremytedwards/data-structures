# coding=utf-8


class Trie(object):
    """
    Example Trie with two token inserts
        token = baa
        token = ball
        { 'b': { 'a': { 'a': { '$' : '$' },
                        'l': { 'l': { '$' : '$' }},
        }    }    }
    """
    def __init__(self):
        self._key = {}
        self._value = "*"

    def insert(self, token):
        """
        Will insert the value token into the trie. If character in token is already present,
        it will be ignored.
        """
        if token:
            cursor = self._key
            for char in token:
                cursor = cursor.setdefault(char, {})
            cursor["$"] = "$"
            return self._key
        else:
            return self._key

    def contains(self, token):
        """
        Will return True if token is in the trie, False if not.
        """
        if token:
            cursor = self._key
            for char in token:
                if char in cursor:
                    cursor = cursor[char]
                else:
                    return False
            if "$" in cursor:
                return True
            else:
                return False

    def traversal(self, start=None, prefix=''):
        """"
        Perform a full depth-first traversal of the graph beginning at start.
        Return: a generator containing all tokens in the trie.
        """
        if start is None:
            start = self._key
        for key in start:
            if key == "$":
                yield prefix
            else:
                for item in self.traversal(start[key], prefix + key):
                    yield item

    def autocomplete(self, token):
        """
        Return a list of words starting with token.
        """
        val = self._key
        for key in token:
            try:
                val = val[key]
            except KeyError:
                return {}
        collectable = [item for item in self.traversal(val, token)]
        if len(collectable) <= 4:
            return collectable
        else:
            return collectable[:4]
