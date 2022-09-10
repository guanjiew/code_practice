from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution121:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        min_sofar = prices[0]
        max_prof = 0
        for price in prices:
            max_prof = max(max_prof, price - min_sofar)
            min_sofar = min(min_sofar, price)
        return max_prof


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution122:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        dp = [[0, 0]] * len(prices)
        dp[0] = [0, -prices[0]]
        for i in range(1, len(prices)):
            # if we don't have a stock on day i, then either we didn't have a stock on day i-1
            # or we sold it on day i
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # if we own stock on day i, then we either buy it on day i or we already own it from day i-1
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        no_share, with_share = 0, -prices[0]
        for i in range(1, len(prices)):
            # if we don't have a stock on day i, then either we didn't have a stock on day i-1
            # or we sold it on day i
            no_share = max(no_share, with_share + prices[i])
            # if we own stock on day i, then we either buy it on day i or we already own it from day i-1
            with_share = max(no_share - prices[i], with_share)
        return no_share

