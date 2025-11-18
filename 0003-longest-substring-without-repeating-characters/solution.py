class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        # Brute Force
        O(n ** 3)

        # Optimized
        - abcabcbb
        - use a dict and two pointers
        - if s[r] != 0:
            - while s[r] != 0:
                - s[l] -= 1
                - l += 1
        - s[r] += 1
        - r += 1
        - update the max
        
        - {}, l, r = 0
        - i = 0: a      {a: 1} , l=0, r=1
        - i = 1: ab     {a: 1, b: 1}, l = 0, r = 2
        - i = 2: abc    {a: 1, b: 1, c: 1}
        - i = 3: a bca   {a: 1, b: 1, c: 1}, l = 1, r = 3
        - i = 4: ab cab  {a: 1, b: 1, c: 1} l = 2, r = 4
        - i = 5: abc abc {a: 1, b: 1, c: 1} l = 3, r = 5
        - i = 6: abc abc b
        """

        # def no_repeating_char(word):
        #     counter = Counter(word)
        #     return all(x == 1 for x in counter.values())
        
        # n = len(s)
        # max_len = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if no_repeating_char(s[i: j + 1]):
        #             max_len = max(max_len, j - i + 1)
        
        # return max_len

        n = len(s)

        if n == 0:
            return 0

        max_len = 0
        l, r = 0, 0
        counter = defaultdict(int)

        while r < n:
            while counter[s[r]] != 0:
                counter[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
            counter[s[r]] += 1
            r += 1
            

        return max_len
            

                

