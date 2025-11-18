class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        if n == 0:
            return 0

        counter = defaultdict(int)
        l, r = 0, 0
        max_freq = 0
        longest = 0

        for r in range(n):   
            counter[s[r]] += 1
            window_size = r - l + 1
            max_freq = max(max_freq, counter[s[r]])
     

            if window_size - max_freq > k:
                counter[s[l]] -= 1
                l += 1

            window_size = r - l + 1
            longest = max(longest, window_size)

        
        return longest


    
