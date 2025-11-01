class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        res = []

        for i in strs:
            key = [0] * 26
            for j in i:
                n = ord(j) - ord("a")
                key[n] += 1
            
            key = tuple(key)
            hashmap[key].append(i)

        for i in hashmap.values():
            res.append(i)

        return res
