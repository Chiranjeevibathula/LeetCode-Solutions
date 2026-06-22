class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize maximum profit and minimum price seen so far
        max_profit = 0
        min_price = float('inf')

        # Iterate through each price in the array
        for current_price in prices:
            # Update maximum profit if selling at current price yields higher profit
            # (current_price - min_price) represents profit if we sell at current price
            max_profit = max(max_profit, current_price - min_price)

            # Update minimum price seen so far for potential future transactions
            min_price = min(min_price, current_price)

        return max_profit

