class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Create a res integer 
        # Starting from the ends of the container
        # While left pointer is less than right pointer
        # Find the current area of water contained and set to max
        # Move the ppointer with lowest height
        res = float("-inf")
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
