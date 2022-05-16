from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.grid = []
        self.n = 0
        self.visited = set()

    def adjacent(self, cell):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for direct in directions:
            new_cell = (direct[0] + cell[0], direct[1] + cell[1])
            if 0 <= new_cell[0] < self.n and 0 <= new_cell[1] < self.n \
                    and not self.grid[new_cell[0]][new_cell[1]] and new_cell not in self.visited:
                yield new_cell

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        self.grid = grid
        self.n = len(grid)
        queue = [(0, 0, 1)]
        self.visited = {(0, 0)}
        while queue:
            x, y, depth = queue.pop(0)
            if x == self.n - 1 and y == self.n - 1:
                return depth
            for adj in self.adjacent((x, y)):
                queue.append((adj[0], adj[1], depth + 1))
                self.visited.add(adj)
        return -1
