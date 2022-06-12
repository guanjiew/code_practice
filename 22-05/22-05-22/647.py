# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.

class Solution:
    def __init__(self):
        self.s = ""
        self.n = 0
    def palindromic_from_centre(self, i, j):
        count = 0
        while i >= 0 and j < self.n:
            if self.s[i] == self.s[j]:
                count += 1
                i -= 1
                j += 1
            else:
                break
        return count

    def countSubstrings(self, s: str) -> int:
        self.s = s
        self.n = len(s)
        total = 0
        for i in range(len(s)):
            total += self.palindromic_from_centre(i, i)
            if i + 1 < len(s):
                total += self.palindromic_from_centre(i, i + 1)
        return total


s = Solution()
print(s.countSubstrings("abc"))
