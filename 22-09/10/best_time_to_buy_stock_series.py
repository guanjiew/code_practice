# Buy & Sell stock series
# Problem pattern: Find the maximum profit from a series of stock prices (buy & sell) with
# some constraints Key assumptions:
# 1. You may not hold multiple stocks at the same time, i.e., you must sell the stock before you buy again.
# This greatly simplifies the problem as you can only have one transaction at a time.
# 2. You may complete as many as k transactions, where k is 1, 2 or a positive number or infinite.
# (Count one sell and one buy as one transaction)
# 3. All prices are positive integers, this implies to obtain a higher profit, it is not reasonable to hold the stock
# at the end of the series, even you might be losing money by doing so.
# 4. Since you are not allowed to hold multiple stocks at the same time, there is no point to perform buy and sell
# on the same day, if you do so, you will not gain any profit. So each day, you can either buy or sell, nor do nothing
# 4. Some problems add other constraints, e.g., transaction fee, cooldown period, etc.

# Problem Strategy:
# Since each day we have a finite number of states, we can use dynamic programming to keep track of the states


from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution121:
    # k = 1, this problem simplifies to finding the largest increase in the series
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
    # k = infinite, we keep track of 2 states for each day: buy and sell
    # buy means we have a stock in hand, sell means we don't have a stock in hand
    # buy state on day i can be reached by either:
    # a. sell state on day i-1 and buy on day i
    # b. buy state on day i-1 and do nothing on day i
    # buy[i] = max(buy[i-1], sell[i-1] - prices[i])
    # sell state on day i can be reached by either:
    # a. buy state on day i-1 and sell on day i
    # b. sell state on day i-1 and do nothing on day i
    # sell[i] = max(sell[i-1], buy[i-1] + prices[i])

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        sell, buy = 0, -prices[0]
        for i in range(1, len(prices)):
            sell, buy = max(sell, buy + prices[i]), max(buy, sell - prices[i])
        return sell


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution714:
    # Apply a transaction fee when selling the stock
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 1:
            return 0
        sell, buy = 0, -prices[0]
        for i in range(1, len(prices)):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution309:
    # Introduced a cooldown state, cooldown state means we sell a stock on previous day
    # Sell state means it is a day we don't have a stock in hand, but not a cooldown day
    # buy state means we have a stock in hand
    # buy state on day i can be reached by either:
    # a. sell state on day i-1 and buy on day i
    # b. buy state on day i-1 and do nothing on day i
    # sell state on day i can be reached by either:
    # a. cooldown state on day i-1 and do nothing on day i
    # b. sell state on day i-1 and do nothing on day i
    # cooldown state on day i can be reached by buy state on day i-1 and sell on day i
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        sell, buy, cooldown = 0, -prices[0], float('-inf')
        for i in range(1, len(prices)):
            buy, sell, cooldown = max(buy, sell - prices[i]), max(sell, cooldown), buy + prices[i]
        return max(sell, cooldown)


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution123:
    # k = 2, we keep track of 4 states for each day: buy1, sell1, buy2, sell2
    # buy1 state on day i can be reached by either:
    # a. buy1 state on day i-1 and do nothing on day i
    # b. buy a stock on day i
    # sell1 state on day i can be reached by either:
    # a. sell1 state on day i-1 and do nothing on day i
    # b. sell a stock on day i
    # buy2 state on day i can be reached by either:
    # a. buy2 state on day i-1 and do nothing on day i
    # b. sell1 state on day i-1 and buy a stock on day i
    # sell2 state on day i can be reached by either:
    # a. sell2 state on day i-1 and do nothing on day i
    # b. buy2 state on day i-1 and sell a stock on day i
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0
        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return max(sell1, sell2)


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution188:
    def maxNoLimit(self, prices: List[int]) -> int:
        sell, buy = 0, -prices[0]
        for i in range(1, len(prices)):
            sell, buy = max(sell, buy + prices[i]), max(buy, sell - prices[i])
        return sell

    def maxProfit(self, k, prices: List[int]) -> int:
        # k is general, we need to keep track of 2k states for each day
        if len(prices) < 1:
            return 0
        if k > len(prices) // 2:
            return self.maxNoLimit(prices)
        buy = [[0] * (k + 1) for _ in range(len(prices))]
        sell = [[0] * (k + 1) for _ in range(len(prices))]
        buy[0][0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i][0] = max(buy[i - 1][0], -prices[i])
        for j in range(1, k + 1):
            buy[0][j] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])
        return max(sell[-1])
