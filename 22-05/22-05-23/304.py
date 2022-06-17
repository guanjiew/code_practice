from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.cache = [[0] * n for i in range(m)]
        for i in range(m):
            row = self.cache[i]
            row[0] = matrix[i][0]
            for j in range(1, n):
                row[j] = row[j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        print(self.cache)
        for row in range(row1, row2 + 1):
            if col1 == 0:
                sum += self.cache[row][col2]
            else:
                sum += (self.cache[row][col2] - self.cache[row][col1 - 1])
        return sum


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)
