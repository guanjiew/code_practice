from typing import List


class Solution:
    def __init__(self):
        self.results = []
        self.permutation = []

    def backtracking(self, remain):
        if not remain:
            self.results.append(self.permutation[:])
        for i in range(0, len(remain)):
            self.permutation.append(remain[i])
            self.backtracking(remain[0:i] + remain[i + 1:])
            self.permutation.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums)
        return self.results
