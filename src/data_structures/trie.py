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
            try:
                test_value = self._key[token[0]]
                self._key[token[0]].insert(token[1:])
            except KeyError:
                self._key[token[0]] = Trie()
                if token[1:]:
                    self._key[token[0]].insert(token[1:])
                else:
                    self._key[token[0]] = {"$": "$"}

    def contains(self, token):
        """
        Will return True if token is in the trie, False if not.
        """
        if token:
            try:
                test_value = self._key[token[0]]
                if test_value == "$":
                    return True
                else:
                    self._key.contains(token[1:])
            except KeyError:
                return False



    def traversal(self, start):
        """"
        Perform a full depth-first traversal of the graph beginning at start.
        Return: a generator containing all tokens in the trie.
        """
        pass
