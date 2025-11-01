class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for i in s:
            n = i
            if (n-1) not in s:
                length = 1
                while (n+1) in s:
                    length += 1
                    n += 1
                res = max(length, res)

        return res
                
