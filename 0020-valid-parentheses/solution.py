class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }
        stack = []

        for i in s:
            if i in closing:
                if stack:
                    if stack.pop() != closing[i]:
                        return False
                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0
