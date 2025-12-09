class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        length = len(candidates)

        def dfs(starting_index, path, curr):
            if curr == target:
                result.append(path.copy())
                return
            if curr > target or starting_index >= length :
                return

            for i in range(starting_index, length):
                path.append(candidates[i])
                dfs(i, path, curr+candidates[i])
                path.pop()
        dfs(0, [], 0)
        return result

