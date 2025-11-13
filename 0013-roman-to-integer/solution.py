class Solution:
    def romanToInt(self, s: str) -> int:

        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        n = len(s)
        i = n - 1
        answer = hashmap[s[i]]

        while i > 0:
            if hashmap[s[i]] <= hashmap[s[i - 1]]:
                answer += hashmap[s[i - 1]]
            else:
                answer -= hashmap[s[i - 1]]
            i -= 1

        return answer

