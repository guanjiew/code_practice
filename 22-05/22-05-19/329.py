"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
***************************************************************
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move
outside the boundary (i.e., wrap-around is not allowed).

***************************************************************
Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1
***************************************************************
Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 231 - 1

***************************************************************
Complexity

TC O(mn)
SC O(mn)
"""

from typing import List


class Solution:
    def __init__(self):
        self.matrix = []
        self.m = 0
        self.n = 0
        self.LP = []

    def validNxt(self, i, j):
        for direction in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
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
        cur_max = 0
        self.m = m
        self.n = n
        self.matrix = matrix
        self.LP = [[-1] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.LP[i][j] == -1:
                    self.LP[i][j] = self.DFS(i, j)
                cur_max = max(cur_max, self.LP[i][j])
        return cur_max
