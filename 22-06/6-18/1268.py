import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.link = collections.defaultdict(TrieNode)
        self.suggestions = []

    def add_suggestion(self, product):
        if len(self.suggestions) < 3:
            self.suggestions.append(product)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        root = TrieNode()
        for product in products:
            trie = root
            for ch in product:
                trie = trie.link[ch]
                trie.add_suggestion(product)
        results = []
        trie = root
        for i, ch in enumerate(searchWord):
            if ch in trie:
                trie = trie.link[ch]
                results.append(trie.suggestions)
            else:
                results.append([] * (len(searchWord) - i))
                break
        return results
