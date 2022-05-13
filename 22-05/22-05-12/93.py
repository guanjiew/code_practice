# https://leetcode.com/problems/restore-ip-addresses/
from typing import List


class Solution:
    def __init__(self):
        self.results = []
        self.ipAddress = " "
        self.lastDot = 0

    def backtracking(self, ipS, startIndex, dots):
        # startIndex: the next available place we can consider inserting dots
        # dots: the number of dot we are trying to insert
        # Stopping when we have successfully inserted all 4 dots
        if dots == 5:
            self.results.append(self.ipAddress[1:])
            return
        # Rules for pruning:
        # 1. If number of remaining digits is 3 times more than the remaining dots, prune it!
        # That is len(s) - 1 - i <= 3 * (4 - dots) and i needs to start from startIndex =>
        # i >= len(s) + 3 * dots - 13 and i >= startIndex
        # 2. If number of remaining digits is less than the remaining dots, prune it!
        # That is len(s) - 1 - i >= 4 - dots =>
        # i <= len(s) + dots - 5
        # 3. If the slice has leading zeros, prune it!
        # 4. If the slice > 255, prune it!
        # After applying all the pruning, we make sure the all results collect in base case are valid
        for i in range(max(startIndex, len(ipS) + 3 * dots - 13), len(ipS) + dots - 4):
            if ipS[startIndex] == '0' and startIndex != i:
                return
            if int(ipS[startIndex:i + 1]) > 255:
                return
            self.lastDot = len(self.ipAddress) - 1
            self.ipAddress += ".{}".format(ipS[startIndex: i + 1])
            self.backtracking(ipS, i + 1, dots + 1)
            last_dot = self.ipAddress.rfind(".")
            if last_dot != -1:
                self.ipAddress = self.ipAddress[: last_dot]

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtracking(s, 0, 1)
        return self.results
