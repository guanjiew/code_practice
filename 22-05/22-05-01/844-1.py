# Define M ,N are the lengths of S and T respectively
# Time Complexity: O(M + N),
# Space Complexity: O(M + N)
def backspaceCompare(s, t):
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)

    return build(s) == build(t)


print(backspaceCompare("a##c", "#a#c"))
