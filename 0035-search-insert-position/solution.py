class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Get pointers left and right
        # While left is less than right
        # Find the mid
        # If the mid index value is target return mid
        # If it less update the left to mid+1
        # If it is greater than the target update the right to mid-1
        # If the value is not found return left
        if len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
                
        return l
