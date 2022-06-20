import collections
from typing import List
Trie = lambda: collections.defaultdict(Trie)

z
def longestCommonPrefix(strs: List[str]) -> str:
    root = Trie()
    for s in strs:
        trie = root
        for c in s:
            if trie["."] in trie:
                break
            trie = trie[c]
        trie["."] = True
    prefix = ""
    trie = root
    while trie["."] not in trie and len(trie) == 1:
        key = list(trie)[0]
        prefix += key
        trie = trie[key]
    return prefix

print(longestCommonPrefix(["happ", "hads"]))

