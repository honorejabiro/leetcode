class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case if the index is equal to length of nums add the path and return
        # Define the result list 
        res = []
        length = len(nums)
        # Define the dfs function
        def dfs(index, path):
            # Base case if the index is equal to length of nums add the path and return
            if index == length:
                res.append(path.copy())
                return
            # Add the path to the result list
            res.append(path.copy())
            # For loop starting from the current index
            for i in range(index, length):
                # Add the number to the path
                path.append(nums[i])
                # Recursively call the function
                dfs(i+1, path)
                # Pop from the list after backtracking
                path.pop()
        # Call the dfs function
        dfs(0, [])
        # Return the result list
        return res

