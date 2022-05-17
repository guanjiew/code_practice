import copy
from typing import List


class Solution:
    def __init__(self):
        self.board = []

    def isValidSudoku(self, row, col, num):
        if str(num) in self.board[row]:
            return False
        for i in range(9):
            if str(num) == self.board[i][col]:
                return False
        matrix = []
        s_row = row // 3 * 3
        s_col = col // 3 * 3
        for i in range(3):
            for j in range(3):
                s = self.board[s_row + i][s_col + j]
                if s != '.':
                    matrix.append(s)
        if str(num) in matrix:
            return False
        return True

    def backtracking(self, r, c) -> bool:
        for i in range(r, 9):
            for j in range(c, 9):
                if self.board[i][j] == '.':
                    for k in range(1, 10):
                        if self.isValidSudoku(i, j, k):
                            self.board[i][j] = str(k)
                            if j < 8 and '.' in self.board[i][j + 1:]:
                                if self.backtracking(i, j + 1):
                                    return True
                            else:
                                if self.backtracking(i + 1, 0):
                                    return True
                            self.board[i][j] = '.'
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.backtracking(0, 0)


s = Solution()
board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(board1)
print(board1)
