class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            target = -nums[i]
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1

        return result
