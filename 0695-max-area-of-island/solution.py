from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def get_neighbors(cell, grid):
            moves = []
            dr = [1, 0, -1, 0]
            dc = [0, 1, 0, -1]
            r, c = cell[0], cell[1]

            for i in range(4):
                nr, nc = dr[i] + r, dc[i] + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    moves.append((nr, nc))
            print(moves)

            return moves

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    q = deque([(r, c)])
                    visited.add((r,c))
                    area = 0
                    while q:
                        length = len(q)
                        for i in range(length):
                            node = q.popleft()
                            area += 1
                            for move in get_neighbors(node, grid):
                                if move not in visited:
                                    visited.add(move)
                                    q.append(move)
                            
                    
                    res = max(res, area)

        return res
