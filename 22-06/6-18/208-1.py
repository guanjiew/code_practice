class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["."] = True

    def _search(self, word, prefix=False):
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        if prefix:
            return True
        else:
            return '.' in t

    def search(self, word):
        return self._search(word)

    def startsWith(self, prefix):
        return self._search(prefix, prefix=True)
