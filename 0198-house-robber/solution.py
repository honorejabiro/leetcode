class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            curr = nums[i]
            tot = 0
            for j in range(0, i-1):
                if nums[j] + curr > tot:
                    nums[i] = nums[j] + curr
                    tot = nums[j] + curr
                    
        return max(nums[-1], nums[-2])
