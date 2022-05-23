from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.results = []
        self.subset = []

    def backtracking(self, index):
        self.results.append(self.subset[:])
        if index == len(self.nums):
            return
        for i in range(index, len(self.nums)):
            self.subset.append(self.nums[i])
            self.backtracking(i + 1)
            self.subset.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.backtracking(0)
        return self.results


s = Solution()
print(s.subsets([1, 2, 3]))
