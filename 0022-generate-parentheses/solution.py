from collections import Counter
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Base case is if the length of 3 is reached add the path
        # If opening is greater than n return or closing or closing
        # If closing is greater than opeing we return
        result = []
        def dfs(path):
            counter = Counter(path)
            opening = counter['('] if '(' in counter else 0
            closing = counter[')'] if ')' in counter else 0
            if opening > n or closing > n or closing > opening:
                return
            
            if len(path) == n*2:
                result.append("".join(path.copy()))
                return

            path.append('(')
            dfs(path)
            path.pop()
            path.append(')')
            dfs(path)
            path.pop()
        
        dfs([])

        return result
