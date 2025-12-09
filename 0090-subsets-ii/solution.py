class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the list
        # Create the dfs function
        # Store the path to the result
        # If the starting index is same as length return
        # Skip duplicates and operate the recurse
        # Backtrack and pop the number from the path
        nums.sort()
        result = []
        length = len(nums)
        def dfs(starting_index, path):
            result.append(path[:])
            if length == starting_index:
                return

            for i in range(starting_index, length):
                if i > starting_index and nums[i-1] == nums[i]:
                    continue

                path.append(nums[i])
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return result
