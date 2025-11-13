class DSU:
    def __init__(self, grid):
        self.parents = {}
        self.sizes = {}
        self.num_islands = 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.parents[(r, c)] = (r, c)
                    self.sizes[(r, c)] = 1
                    self.num_islands += 1

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):

        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        if self.sizes[parent_x] > self.sizes[parent_y]:
            self.parents[parent_y] = parent_x
            self.sizes[parent_x] += self.sizes[parent_y]
        else:
            self.parents[parent_x] = parent_y
            self.sizes[parent_y] += self.sizes[parent_x]

        self.num_islands -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dsu = DSU(grid)
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                            dsu.union((r, c), (nr, nc))

        return dsu.num_islands

