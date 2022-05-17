from typing import List


class Solution:
    def __init__(self):
        self.board = []
        self.n = 0
        self.solutions = []

    def isValidQueen(self, row, col):
        for i in range(0, row):
            if self.board[i][col]:
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while j < self.n and i >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j += 1
        return True

    def draw(self):
        res = []
        for i in range(self.n):
            row = ""
            for j in range(self.n):
                if self.board[i][j] == 0:
                    row += "."
                else:
                    row += "Q"
            res.append(row)
        return res

    def backtracking(self, row):
        if row == self.n:
            if 1 in self.board[self.n - 1]:
                self.solutions.append(self.draw())
            return
        for col in range(self.n):
            if not self.board[row][col] and self.isValidQueen(row, col):
                self.board[row][col] = 1
                self.backtracking(row + 1)
                self.board[row][col] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.backtracking(0)
        return self.solutions


s = Solution()
for i in range(1, 20):
    print(i, len(s.solveNQueens(i)))
