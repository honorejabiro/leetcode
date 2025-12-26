class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [float('-inf')] * (target+1)
        dp[0] = 0

        for x in nums:
            for j in range(target, x-1, -1):
                if dp[j - x] != float('-inf'):
                    dp[j] = max(dp[j], dp[j - x] + 1)

        return dp[target] if dp[target] != float('-inf') else -1
