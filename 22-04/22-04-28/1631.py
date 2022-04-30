# https://leetcode.com/problems/path-with-minimum-effort/
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dist = [float("inf")] * (n * m)
        dist[0] = 0
        pq = [(0, 0)]
        visited = set()
        while pq:
            weight, vertex = heapq.heappop(pq)
            x, y = vertex // m, vertex % m
            if (x, y) == (n - 1, m - 1):
                break
            if x * m + y in visited:
                continue
            visited.add(x * m + y)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < n and 0 <= ny < m and nx * m + ny not in visited:
                    new_max = max(weight, abs(heights[x][y] - heights[nx][ny]))
                    if new_max < dist[nx * m + ny]:
                        heapq.heappush(pq, (new_max, nx * m + ny))
                        dist[nx * m + ny] = new_max
        return dist[m * n - 1]