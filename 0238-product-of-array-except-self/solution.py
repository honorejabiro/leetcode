class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[:]
        num = 1
        for i in range(1, len(nums)):
            num *= nums[i-1]
            prefix[i] = num
        prefix[0] = 1
        
        suffix = nums[:]
        p = 1
        for j in range(len(nums)-2, -1, -1):
            p *= nums[j+1]
            suffix[j] = p
        suffix[-1] = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]          
        
        return res
