class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Identify the result list
        # Base case if the length of the path equals the length of nums add the path to the result list
        # Define the dfs function
        # For loop of the nums
        # If number in the path skip it
        # Add the number to the path and recursively call the function
        # Pop from the path

        result = []
        length = len(nums)
        visited = [False] * len(nums)

        def dfs(path):
            if len(path) == length:
                result.append(path[:])
                return 

            for i in range(length):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                visited[i] = False

        dfs([])
        return result
