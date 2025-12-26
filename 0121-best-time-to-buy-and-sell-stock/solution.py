class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer = prices[0]
        result = float('-inf')
        r = 1

        while r < len(prices):
            result = max(result, prices[r] - pointer)
            if pointer > prices[r]:
                pointer = prices[r]

            r += 1

        return result if result > 0 else 0
