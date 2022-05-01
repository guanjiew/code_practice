# https://leetcode.com/problems/backspace-string-compare/
# We start traversing from the end of both string, if we encounter k '#',
# then we will skip the next k char that is not '#'
# Define M ,N are the lengths of S and T respectively
# Time Complexity: O(M + N),
# Space Complexity: O(1)

def backspaceCompare(s: str, t: str) -> bool:
    ps, pt = len(s) - 1, len(t) - 1

    def nxt_valid_ptr(x, ptr):
        k = 0
        while ptr >= 0:
            if x[ptr] == '#':
                k += 1
                ptr -= 1
            elif k > 0:
                k -= 1
                ptr -= 1
            else:
                break
        return ptr

    while ps >= 0 or pt >= 0:
        ps, pt = nxt_valid_ptr(s, ps), nxt_valid_ptr(t, pt)
        if (ps >= 0 and pt >= 0 and s[ps] != t[pt]) or ((pt >= 0) != (ps >= 0)):
            return False
        ps -= 1
        pt -= 1
    return True


print(backspaceCompare("a##c", "#a#c"))
