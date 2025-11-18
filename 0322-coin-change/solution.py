class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(n):
            for curr_amount in range(amount + 1):
                if curr_amount >= coins[i]:
                    dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount - coins[i]])
        
        return dp[-1] if dp[-1] != float("inf") else -1
