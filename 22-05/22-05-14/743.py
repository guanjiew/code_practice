# https://leetcode.com/problems/network-delay-time/
import heapq
from typing import List


class Solution:
    def __init__(self):
        self.edges = {}
        self.vertices = []
        self.visited = []
        self.unexplored = []
        self.dist = []

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.vertices = [i for i in range(n)]
        for i in range(n):
            self.edges[i] = []
        for edge in times:
            self.edges[edge[0] - 1].append([edge[1] - 1, edge[2]])
        self.dist = [float('inf') for i in range(n)]
        self.dist[k-1] = 0
        heapq.heappush(self.unexplored, (0, k - 1))
        while self.unexplored:
            _, vertex = heapq.heappop(self.unexplored)
            self.visited.append(vertex)
            for neigh in self.edges[vertex]:
                (w, cost) = neigh
                if w not in self.visited and cost + self.dist[vertex] < self.dist[w]:
                    self.dist[w] = self.dist[vertex] + cost
                    heapq.heappush(self.unexplored, (cost + self.dist[vertex], w))
        res = max(self.dist)
        if res == float('inf'):
            return - 1
        return res


s = Solution()
print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
