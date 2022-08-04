# https://leetcode.com/problems/generate-parentheses/
from typing import List


# KEY STEP:
# Only add a "(" if we have not used up all the "("
# Only add a ")" if there are more "(" than ")"
# These ensures that we have a valid parenthesis.
# We use backtracking to generate all the possible parenthesis.


def generateParenthesis(n: int) -> List[str]:
    ans = []

    def backtrack(S, left, right):
        if left == right == n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:
            S.append(")")
            backtrack(S, left, right + 1)
            S.pop()

    backtrack([], 0, 0)
    return ans


# Time Complexity: Catalan number O(Cn)

if __name__ == "__main__":
    print(generateParenthesis(3))
