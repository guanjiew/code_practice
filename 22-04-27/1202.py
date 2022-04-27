# https://leetcode.com/problems/smallest-string-with-swaps/
import copy
from typing import List


def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    G = [[] for i in range(n)]
    for pair in pairs:
        source, dest = pair[0], pair[1]
        G[source].append(dest)
        G[dest].append(source)
    visited = [0] * n

    def DFS(src):
        visited[src] = 1
        stack = [src]
        connected = []
        while stack:
            vertex = stack[-1]
            if not visited[vertex]:
                visited[vertex] = 1
            pop = True
            for neigh in G[vertex]:
                if not visited[neigh]:
                    stack.append(neigh)
                    pop = False
                    break
            if pop:
                connected.append(vertex)
                stack.pop()
        return connected

    answer = [""] * n
    for i in range(n):
        if not visited[i]:
            connected_nodes = DFS(i)
            indexes = copy.deepcopy(connected_nodes)
            connected_nodes.sort(key=lambda x: s[x])
            indexes.sort()
            for j in range(len(indexes)):
                answer[indexes[j]] = s[connected_nodes[j]]
    return "".join(answer)


print(smallestStringWithSwaps("dcab",[[0,3],[1,2],[0,2]]))
