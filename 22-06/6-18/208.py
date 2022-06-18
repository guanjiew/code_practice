class TrieNode:
    def __init__(self):
        self.link = [None] * 26
        self.isEnd = False

    def put(self, ch, node):
        self.link[ord(ch) - ord('a')] = node

    def gets(self, ch):
        return self.link[ord(ch) - ord('a')]

    def setEnd(self):
        self.isEnd = True

    def contains(self, ch):
        return self.gets(ch) is not None


class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.trie
        for i in range(len(word)):
            if not trie.contains(word[i]):
                trie.put(word[i], TrieNode())
            trie = trie.gets(word[i])
        trie.setEnd()

    def search(self, word: str) -> bool:
        trie = self.trie
        for i in range(len(word)):
            if not trie.contains(word[i]):
                return False
            trie = trie.gets(word[i])
        if not trie.isEnd:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for i in range(len(prefix)):
            if not trie.contains(prefix[i]):
                return False
            trie = trie.gets(prefix[i])
        return True


# Your Trie object will be instantiated and called as such:
word = "hello"
prefix = "hl"
obj = Trie()
obj.insert(word)
print(obj.search(word))
print(obj.startsWith(prefix))
