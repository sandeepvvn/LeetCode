from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        
        # Capture all positive price differences
        # If price increases from day i to i+1, we can buy on day i and sell on day i+1
        for i in range(len(prices) - 1):
            curr_profit = prices[i + 1] - prices[i]
            if curr_profit > 0:
                total_profit += curr_profit
        
        return total_profit
