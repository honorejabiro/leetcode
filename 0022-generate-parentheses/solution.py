class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []

        def f(length, opening, closing, path):

            if length == 2 * n:
                answer.append("".join(path))
                return
            
            if opening < n:
                path.append("(")
                f(length + 1, opening + 1, closing, path)
                path.pop()
            
            if opening > closing:
                path.append(")")
                f(length + 1, opening, closing + 1, path)
                path.pop()
        
        f(0, 0, 0, [])
        return answer

