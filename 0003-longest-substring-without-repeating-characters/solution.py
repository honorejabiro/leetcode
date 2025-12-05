from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a queue
        # Create a res variable
        # Iterate over the string
        # If element is in the queue
        # Popleft until the element is removed
        # Update the result answer

        res = 0
        queue = deque([])

        for i in s:
            while i in queue:
                queue.popleft()

            queue.append(i)
            res = max(res, len(queue))
        
        return res
