class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(cell, grid, index, visited):
            nonlocal word
            r, c = cell[0], cell[1]
            if index == len(word):
                return True
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != word[index]) or (r, c) in visited:
                return False
            visited.add((r, c))
            res =  (dfs((r-1, c), grid, index+1, visited) or
                dfs((r, c+1), grid, index+1, visited) or
                dfs((r+1, c), grid, index+1, visited) or
                dfs((r, c-1), grid, index+1, visited))
            visited.remove((r, c))
            return res
            

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs((r,c), board, 0, set()):
                        return True

        return False
