class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                tot = nums[l] + nums[r]
                if tot == target:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    r -= 1
                    l += 1
                elif tot > target:
                    r -= 1
                elif tot < target:
                    l += 1
        return [list(i) for i in res]
