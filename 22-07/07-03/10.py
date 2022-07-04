class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        matches = bool(s) and p[0] in [s[0], "."]
        if len(p) >= 2 and p[1] == "*":
            return (self.isMatch(s, p[2:])) or (matches and self.isMatch(s[1:], p))
        else:
            return matches and self.isMatch(s[1:], p[1:])
