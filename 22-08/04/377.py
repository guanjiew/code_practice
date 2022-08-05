from typing import List


# define subproblem dp[i] as the number of ways to sum to i
# dp[i] = sum (1 + dp[i-k] for k in nums)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= target:
                    dp[i] += dp[i - num]
        return dp[target]
