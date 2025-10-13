class Solution:
    def countVowelPermutation(self, n: int) -> int:

        MOD = 10**9 + 7

        hashmap = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        count = 0

        @lru_cache
        def f(vowel, length):

            if length == n:
                return 1

            res = 0
            for child in hashmap[vowel]:
                res += f(child, length + 1)
            return res

        total = 0
        for vowel in hashmap:
            total += f(vowel, 1)

        return total % MOD

