import collections
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        Trie = lambda: collections.defaultdict(Trie)
        root = Trie()
        tokens = []
        for word in set(words):
            trie = root
            for c in word[::-1]:
                trie = trie[c]
            tokens.append((trie, len(word) + 1))
        return sum(size for node, size in tokens if len(node) == 0)
