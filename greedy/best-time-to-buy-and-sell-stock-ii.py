from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # Initialize max_profit to 0

        # Iterate through the list of prices, starting from the second day
        for i in range(1, len(prices)):
            # Calculate the price difference between the current day and the previous day
            profit = prices[i] - prices[i - 1]

            # If the profit is positive, add it to max_profit (buy and sell on the same day)
            if profit > 0:
                max_profit += profit

        # Return the maximum profit
        return max_profit
