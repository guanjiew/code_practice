from typing import List


class Solution:
    def __init__(self):
        self.matrix = []
        self.m = 0
        self.n = 0
        self.LP = []

    def validNxt(self, i, j):
        valid_directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        for direction in valid_directions:
            grid = (direction[0] + i, direction[1] + j)
            if 0 <= grid[0] < self.m and 0 <= grid[1] < self.n \
                    and self.matrix[grid[0]][grid[1]] > self.matrix[i][j]:
                yield grid

    def DFS(self, i, j):
        cur_max = 0
        for ni, nj in self.validNxt(i, j):
            if self.LP[ni][nj] == -1:
                self.LP[ni][nj] = self.DFS(ni, nj)
            cur_max = max(cur_max, self.LP[ni][nj])
        return cur_max + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        self.m = m
        self.n = n
        self.matrix = matrix
        self.LP = [[-1] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.LP[i][j] == -1:
                    self.LP[i][j] = self.DFS(i, j)
        return max([max(self.LP[i]) for i in range(m)])


s = Solution()
print(s.longestIncreasingPath([[1, 2]]))
print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
