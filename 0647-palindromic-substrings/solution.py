class Solution:
    def countSubstrings(self, s: str) -> int:

        # From the sides
        n = len(s)
        palindromes = n

        # Odd length palindromes
        for c in range(n):
            l, r = c - 1, c + 1
            while l >= 0 and r < n and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

        # Even length palindromes
        for c1 in range(n - 1):
            c2 = c1 + 1

            if s[c1] == s[c2]:
                palindromes += 1

                l, r = c1 - 1, c2 + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    palindromes += 1
                    l -= 1
                    r += 1

        return palindromes

