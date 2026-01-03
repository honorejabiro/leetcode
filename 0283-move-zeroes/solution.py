class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create a left and right pointer
        # Both pointers start at index 0
        # If pointer left is 0 don't move it
        # Move right and if right is a number swap if left is 0
        # Move right 

        l, r = 0, 0
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1

            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            
            elif nums[l] != 0 and nums[r] != 0:
                l += 1
                r += 1


            
