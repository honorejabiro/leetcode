class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Base case if the word is greater than the word target, if the path is equal to the word change the result variable to True
        # Create a visited list
        # We need a visited data structure for our cell iteration
        # We need a visited set for our dfs function parameters: cell, grid
        # Define a neighbors function
        # Create a truth variable default False
        # Get the neighbors
        # Itearte over the returned moves
        # Add the move to the path 
        # Pop from the path
        length = len(word)
        answer = False
        truth = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def get_neighbors(cell, grid):
            new_r = [-1, 0, 1, 0]
            new_c = [0, 1, 0, -1]
            moves = []

            for i in range(4):
                nr = cell[0] + new_r[i]
                nc = cell[1] + new_c[i]
                
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    moves.append((nr, nc))

            return moves
        
        def dfs(cell, grid, path, truth):
            nonlocal answer
            if answer:
                return
            r0, c0 = cell
            path.append(grid[r0][c0])
            truth[r0][c0] = True

            if len(path) == length:
                if ''.join(path) == word:
                    answer = True
                truth[r0][c0] = False
                path.pop()
                return
            for r, c in get_neighbors(cell, grid):
                if truth[r][c]:
                    continue
                if grid[r][c] == word[len(path)]:
                    dfs((r, c), grid, path, truth)
            truth[r0][c0] = False
            path.pop()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if answer:
                    return True
                if board[r][c] == word[0]:   
                    dfs((r, c), board, [], truth)

        return answer
