class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        length = len(s)
        def is_palindrome(strs):
            if strs[:] == strs[::-1]:
                return True

            return False

        def dfs(index, path):
            if index == length:
                result.append(path[:])
                return

            for i in range(index, length):
                if is_palindrome(s[index:i+1]):
                    path.append(s[index:i+1])
                    dfs(i+1, path)
                    path.pop()

        dfs(0, [])
        return result
