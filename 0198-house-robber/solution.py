class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums) 
        def dfs(index):
            if index == len(nums) - 2:
                dp[index] = nums[index]
                return dp[index]

            if index == len(nums) - 1:
                dp[index] = nums[index]
                return dp[index]

            if dp[index] is not None:
                return dp[index]

            ans = nums[index]
            dp[index] = ans

            for i in range(index+2, len(nums)):
                dp[index] = max(dp[index], (ans + dfs(i)))
            return dp[index]

        ans = 0

        for i in range(len(nums)):
            ans = max(ans, dfs(i))

        return ans
