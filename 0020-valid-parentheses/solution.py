class Solution:
    def isValid(self, s: str) -> bool:
        # Create a hashmp to represent the closing brckets
        # Create a stack
        # Iterate over the string
        # If the string is closing Check the stack last element if it is different return False
        # Add the string to the stack
        # Return True if the stack is empty
        hashmap = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        stack = []
        for i in s:
            if i in hashmap:
                if len(stack) == 0 or stack[-1] != hashmap[i]:
                    return False
                stack.pop()

            else:
                stack.append(i)

        return len(stack) == 0

