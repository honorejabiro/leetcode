class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = []
        s = s.strip()
        for i in s:
            if i.isalnum():
                words.append(i)

        l, r = 0, len(words) - 1
        while l < r:
            if words[l].lower() != words[r].lower():
                return False

            l += 1
            r -= 1

        return True
