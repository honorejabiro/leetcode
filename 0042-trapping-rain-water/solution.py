class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        l, r = 0, n - 1
        max_left, max_right = 0, 0
        trapped = 0

        while l < r:
            if height[l] < height[r]:
                max_left = max(height[l], max_left)
                trapped += max_left - height[l]
                l += 1
            else:
                max_right = max(height[r], max_right)
                trapped += max_right - height[r]
                r -= 1
        
        return trapped
