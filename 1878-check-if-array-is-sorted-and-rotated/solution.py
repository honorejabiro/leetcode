class Solution:
    def check(self, nums: List[int]) -> bool:
        moved = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                moved = i
        i = (moved + 1) % len(nums)

        while i%len(nums) != moved:
            if nums[(i)%len(nums)] < nums[(i-1)%len(nums)]:
                return False

            i += 1


        return True

