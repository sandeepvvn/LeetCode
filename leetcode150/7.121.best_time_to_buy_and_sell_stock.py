from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy: index of the minimum price seen so far (candidate buy day)
        buy = 0
        # sell: index we use to scan future days (candidate sell day)
        sell = 1
        max_profit = 0
        while sell < len(prices):
            # If selling today yields a better profit, update the answer
            if prices[sell] - prices[buy] > max_profit:
                max_profit = prices[sell] - prices[buy]
            # If we find a cheaper price, move buy pointer to this day
            elif prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return max_profit