class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_left, max_right = 0, 0
        area = 0
        while l < r:
            if height[l] < height[r]:
                add = max_left - height[l]
                if add > 0:
                    area += add
                max_left = max(max_left, height[l])
                l += 1
            else:
                add = max_right - height[r]
                if add > 0:
                    area += add
                max_right = max(max_right, height[r])
                r -= 1

        return area
