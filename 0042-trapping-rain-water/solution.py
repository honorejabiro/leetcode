class Solution:
    def trap(self, height: List[int]) -> int:
        curr_left, curr_right = 0, 0
        l, r = 0, len(height) - 1
        result = 0

        while l <= r:
            if curr_left > curr_right:
                temp = curr_right - height[r]
                if temp > 0:
                    result += temp
                else:
                    curr_right = height[r]
                r -= 1

            else:
                temp = curr_left - height[l]
                if temp > 0:
                    result += temp
                else:
                    curr_left = height[l]
                l += 1

        return result
