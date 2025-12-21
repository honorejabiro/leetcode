from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a queue
        # Create a result variable
        # Iterate the string
        # Create a set
        # Update the result variable using the length of the queue
        # If the string is in the set
        # We remove the end of the queue and remove from the set
        # Add to the queue
        queue = deque([])
        res = 0
        duplicates = set()

        for i in range(len(s)):
            while s[i] in duplicates:
                n = queue.popleft()
                duplicates.remove(n)
            
            queue.append(s[i])
            duplicates.add(s[i])
            res = max(len(queue), res)

        return res

