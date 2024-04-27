from typing import List


# https://leetcode.com/problems/island-perimeter/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r in (-1, ROWS) or c in (-1, COLS) or
                    grid[r][c] == 0):
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1  # mark visited
            return (dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))

        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    perimeter += dfs(r, c)

        return perimeter
