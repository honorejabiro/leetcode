from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Result array
        # Create a hashmap of the key
        # Itearte the arrrsy and create the key
        # If key in hashmap add teh word
        # Return the list of the anagrams
        res = []
        hashmap = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for i in word:
                key[ord(i) - ord('a')] += 1
            hashmap[tuple(key)].append(word)


        for j in hashmap.values():
            res.append(j)

        return res
