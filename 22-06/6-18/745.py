from typing import List


class WordFilter:

    def _insert(self, trie, word, idx, prefix=True):
        if not prefix:
            word = word[::-1]
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]

    def __init__(self, words: List[str]):
        self.prefix_trie = {}
        self.suffix_trie = {}
        for idx, word in enumerate(words):
            self._insert(self.suffix_trie, word, idx)
            self._insert(self.suffix_trie, word, idx, prefix=False)

    def _search(self, trie, word, prefix=True):
        if not prefix:
            word = word[::-1]
        for c in word:
            if c not in trie:
                return False
        return True

    def f(self, prefix: str, suffix: str) -> int:
        index = -1
        length = 0

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
