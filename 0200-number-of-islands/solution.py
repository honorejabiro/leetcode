from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Create a visted set
        # Define the get neighbors function return valid moves to make
        # Define the number of islands variable
        # Iterate over the cells in my matrix
        # If the cell is not in visitesd array
        # Operate a dfs function
        # Update the number of islands
        number_of_islands = 0
        visited = set()
        def get_neighbors(cell, grid):
            r, c = cell[0], cell[1]
            dr = [1, 0 , -1, 0]
            dc = [0, 1, 0, -1]
            moves = []

            for i in range(4):
                nr, nc = dr[i]+r, dc[i]+c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    moves.append((nr, nc))

            return moves

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    q = deque([(r, c)])
                    visited.add((r,c))

                    while q:
                        length = len(q)
                        for i in range(length):
                            node = q.popleft()
                            for move in get_neighbors((node[0], node[1]), grid):
                                if move not in visited:
                                    visited.add(move)
                                    q.append(move)
                    number_of_islands += 1


        return number_of_islands

