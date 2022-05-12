# https://leetcode.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(k, n, startIndex):
            if sum(path) > n:
                return
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return
            for i in range(startIndex, 10 - (k - len(path)) + 1):
                path.append(i)
                backtracking(k, n, i + 1)
                path.pop()

        backtracking(k, n, 1)
        return result
