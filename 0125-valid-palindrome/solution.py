class Solution:
    def isPalindrome(self, s: str) -> bool:

        # parse the string
        t = []

        for char in s:
            if char.isalnum():
                t.append(char.lower())

        l, r = 0, len(t) - 1

        while l < r:
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1

        return True

