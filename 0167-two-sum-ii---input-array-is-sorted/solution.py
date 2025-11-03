class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using binary search
        # Create a left and right pointer
        # While left is less or equal to right
        # Find the middle number
        # Move the pointers according to the middle 
        # If the total is target return a list of left and right
        l, r = 0, len(numbers) - 1
        while l <= r:
            tot = numbers[l] + numbers[r]
            if tot == target:
                return [l+1, r+1]
            elif tot > target:
                r -= 1
            elif tot < target:
                l += 1

        
