class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the list of candidates
        # Define the result list
        # Define the length variable
        # Define the function
        # Base case if the index equals the length or sum greater than target of candidates return 
        # If target equals the target add to the result list
        # For loop starting from current index
        # If the number is the same as previous number skip
        # Recurse and after backtracking pop from the path
        candidates.sort()
        result = []
        length = len(candidates)

        def dfs(index, path, tot):
            if tot == target:
                result.append(path[:])
                return
            if index == length or tot > target:
                return

            for i in range(index, length):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                dfs(i+1, path, tot+candidates[i])
                path.pop()

        dfs(0, [], 0)
        return result
