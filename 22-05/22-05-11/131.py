# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


def checkPalindrome(s):
    return s == s[::-1]


class Solution:
    def __init__(self):
        self.results = []
        self.part = []

    def backtracking(self, s, startIndex):
        if startIndex == len(s):
            self.results.append(self.part[:])
            return
        for i in range(startIndex, len(s)):
            if not checkPalindrome(s[startIndex: i + 1]):
                continue
            self.part.append(s[startIndex: i + 1])
            self.backtracking(s, i + 1)
            self.part.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.results


S = Solution()
print(S.partition("aab"))
