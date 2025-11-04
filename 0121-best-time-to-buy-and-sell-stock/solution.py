class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep a current minimum
        # Iterate the list
        # If the current index ha a number greater find the profit and update the profit by max
        # Update the minimum buying price
        curr_min = prices[0]
        profit = 0
        for i in prices[1:]:
            if i > curr_min:
                p = i - curr_min
                profit = max(profit, p)
            if i < curr_min:
                curr_min = i

        return profit
