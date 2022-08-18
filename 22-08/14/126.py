from typing import List


def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    # build a graph based on the wordList, create edges between words that differ by one letter
    graph = {}
    for word in wordList:
        for i in range(len(word)):
            s = word[:i] + '_' + word[i + 1:]
            graph[s] = graph.get(s, []) + [word]

    print(graph)
    # BFS to find all paths from beginWord to endWord
    queue = [(beginWord, [beginWord])]
    res = []
    found = False
    while queue:
        word, path = queue.pop(0)
        if found and len(path) > len(res[0]):
            break
        if word == endWord:
            res.append(path)
            found = True
        for i in range(len(word)):
            s = word[:i] + '_' + word[i + 1:]
            for w in graph.get(s, []):
                if w not in path:
                    queue.append((w, path + [w]))

    return res


def findLadders2(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    # build a graph based on the wordList, create edges between words that differ by one letter
    graph = {}
    for word in wordList:
        for i in range(len(word)):
            s = word[:i] + '_' + word[i + 1:]
            graph[s] = graph.get(s, []) + [word]

    print(graph)
    # bidirectional BFS to find all shortest paths from beginWord to endWord
    queue = [(beginWord, [beginWord])]
    queue2 = [(endWord, [endWord])]
    res = []
    found = False
    visited1 = set()
    visited2 = set()
    while queue and queue2:
        word, path = queue[0]
        word2, path2 = queue2[0]
        if found and len(path) + len(path2) > len(res[0]) + 1:
            break
        if word == word2:
            print(path, path2)
            res.append(path + path2[:-1][::-1])
            found = True
        if len(queue) < len(queue2):
            queue.pop(0)
            for i in range(len(word)):
                s = word[:i] + '_' + word[i + 1:]
                for w in graph.get(s, []):
                    if w not in path and w not in visited1:
                        queue.append((w, path + [w]))
                        visited1.add(w)
        else:
            queue2.pop(0)
            for i in range(len(word2)):
                s = word2[:i] + '_' + word2[i + 1:]
                for w in graph.get(s, []):
                    if w not in path2 and w not in visited2:
                        queue2.append((w, path2 + [w]))
                        visited2.add(w)

    return res


if __name__ == '__main__':
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # print(findLadders("hit", "cog", wordList))
    print(findLadders2("hit", "cog", wordList))
    # [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
