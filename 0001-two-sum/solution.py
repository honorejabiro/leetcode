from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = defaultdict()
        answer = []

        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if (nums[i]) in difference:
                answer.append(difference[nums[i]])
                answer.append(i)
                return answer
            difference[diff] = i
            i += 1


