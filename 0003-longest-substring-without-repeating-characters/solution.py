class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a left and right pointer pointing at index 0
        # While right pointer is less than length of the string
        # Check if the string is in the set, if it is update the length of the substring max
        # Update the pointers
        # Return the longest substring
        if len(s) == 0:
            return 0
        visited = set()
        longest = 0
        n = len(s)
        l, r = 0, 0
        while r < n:
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            longest = max(longest, len(visited))
            r += 1
        return longest
