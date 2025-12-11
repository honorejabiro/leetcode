class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base is the length of the string
        # Create a hashmap mapping the integer to the strings
        # # Using index to keep track of our limit
        if len(digits) == 0:
            return []
        res = []
        length = len(digits)
        hashmap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def dfs(index, path):
            if index == length:
                res.append("".join(path[:]))
                return 

            for i in hashmap[str(digits[index])]:
                path.append(i)
                dfs(index+1, path)
                path.pop()

        dfs(0, [])
        return res
