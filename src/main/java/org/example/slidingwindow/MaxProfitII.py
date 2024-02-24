from typing import List

# Best time to buy and sell stock II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        profit = 0
        # take positive daily return only
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit
