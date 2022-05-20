# https://leetcode.com/problems/unique-paths-ii/
"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e.,
grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move
either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any
square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Constraints:

    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.

"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        if grid[m - 1][n - 1]:
            return 0
        path = [[0] * n for j in range(m)]
        lr_obstacle = -1
        for i in range(n - 1, -1, -1):
            if grid[m - 1][i] == 1:
                lr_obstacle = i
                break
        path[m - 1][lr_obstacle + 1:n] = [1] * (n - lr_obstacle - 1)
        lc_obstacle = -1
        for j in range(m - 1, -1, -1):
            if grid[j][n - 1] == 1:
                lc_obstacle = j
                break
        for j in range(lc_obstacle + 1, m):
            path[j][n - 1] = 1
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if grid[i][j] == 0:
                    path[i][j] = path[i][j + 1] + path[i + 1][j]
        return path[0][0]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0]]))
