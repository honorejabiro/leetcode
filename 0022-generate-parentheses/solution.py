class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Base case if the closing is greater than opening, if the opeing or clsing is greater than n
        # Define the result list
        # Define the dfs function
        # If the the length of the divided by 2 is equal to n add the path copy to the result
        # Add the opening bracket to the path
        # Recurse the function
        # After backtracking
        # Pop from the list
        # Add the closing bracket to the path
        # Call the function 
        # Return the result list
        result = []

        def dfs(path, opening, closing):
            if closing > opening or closing > n or opening > n:
                return

            if len(path)/2 == n:
                result.append(''.join(path.copy()))
                return

            path.append("(")
            dfs(path, opening+1, closing)
            path.pop()
            path.append(")")
            dfs(path, opening, closing+1)
            path.pop()

        dfs([], 0, 0)
        return result

