class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex = {}

        def dp(i, j):
            if (i, j) not in regex:
                if j == len(p):
                    regex[(i, j)] = i == len(s)
                else:
                    matches = i < len(s) and p[j] in [s[i], "."]
                    if len(p[j:]) >= 2 and p[j + 1] == "*":
                        regex[(i, j)] = dp(i, j + 2) or (matches and dp(i + 1, j))
                    else:
                        regex[(i, j)] = matches and dp(i + 1, j + 1)
            return regex[(i, j)]

        return dp(0, 0)
