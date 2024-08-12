from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ROWS2, COLS2 = 3 * ROWS, 3 * COLS
        grid2 = [[0] * COLS2 for _ in range(ROWS2)]

        # scale the grid up
        for r in range(ROWS):
            for c in range(COLS):
                r2, c2 = 3 * r, 3 * c
                if grid[r][c] == "/":
                    # mark grid2 cells as 1 from top right to bottom left
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[r][c] == "\\":
                    # mark grid2 cells as 1 from top left to bottom right
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1

        def dfs(r, c, visit):
            if (r in (-1, ROWS2) or c in (-1, COLS2) or
                    grid2[r][c] != 0 or (r, c) in visit):
                return
            visit.add((r, c))
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                dfs(nr, nc, visit)

        visit = set()
        regions = 0
        for r in range(ROWS2):
            for c in range(COLS2):
                if grid2[r][c] == 0 and (r, c) not in visit:
                    dfs(r, c, visit)
                    regions += 1
        return regions
