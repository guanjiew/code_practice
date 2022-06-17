from typing import List

# Define OZ as the largest subset of strs when at most m 0 and n 1 inside
# Then we have
# OZ[m][n] = max(OZ[m][n], 1 + OZ[m - #0 in i_k][n - #1 in i_k], for i_k in strs)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        OZ = [[0] * (n+1) for i in range(m+1)]
        for s in strs:
            ones = s.count("1")
            zeros = s.count("0")
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    OZ[i][j] = max(OZ[i][j], 1+OZ[i-zeros][j-ones])
        return OZ[m][n]

