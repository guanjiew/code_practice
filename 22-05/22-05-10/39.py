# https://leetcode.com/problems/combination-sum/
class Solution:
    def __init__(self):
        self.answers = []
        self.combo = []

    def combinationSum(self, candidates, target: int):
        self.backtracking(candidates, target, 0)
        return self.answers

    def backtracking(self, candidates, target, startIndex):
        if sum(self.combo) >= target:
            if sum(self.combo) == target:
                self.answers.append(self.combo[:])
            return
        for i in range(startIndex, len(candidates)):
            if sum(self.combo) + candidates[i] > target:
                continue
            self.combo.append(candidates[i])
            self.backtracking(candidates, target, i)
            self.combo.pop()
