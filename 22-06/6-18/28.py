class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return -1
        for i in range(len(haystack)-len(needle)):
            start = i
            for j in range(len(needle)):
                if needle[j] != haystack[start]:
                    break
                start += 1
            if start - i == len(needle):
                return i
        return -1
