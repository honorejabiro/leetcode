class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the numbers
        # Get the product of the last three numbers 
        # Return the product 
        nums.sort()
        product = None
        if len(nums) > 3:
            if (nums[0] * nums[1] * nums[-1]) > (nums[-3] *nums[-2] * nums[-1]):
                product = nums[0] * nums[1] * nums[-1]
            else:
                product = nums[-1] * nums[-2] * nums[-3]
        else:
            product = nums[-1] * nums[-2] * nums[-3]
        return product
