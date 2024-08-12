from typing import List


class Solution:
    # Intuition: There are 3 cases
    # 1. If num of Islands in grid are disconnected, meaning numIslands == 0
    # or > 1, return 0
    # 2. If by removing 1 cell numIslands becomes == 0 or > 1, return 1
    # 3. If by removing 2 cells, numIslands becomes == 0 or > 1, return 2
    # We would have to remove at most 2 cells in any case because removing
    # diagonal cells disconnects the island
    # T: O((N * M)^2), M: O(N * M)
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if (r in (-1, ROWS) or c in (-1, COLS) or
                    grid[r][c] == 0 or (r, c) in visit):
                return
            visit.add((r, c))
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                dfs(nr, nc, visit)

        def numOfIslands() -> int:
            visit = set()
            count = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] and (r, c) not in visit:
                        dfs(r, c, visit)
                        count += 1
            return count

        # Case 1
        if numOfIslands() != 1:
            return 0

        # Now we try case 2
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: continue

                grid[r][c] = 0  # turn land into water
                if numOfIslands() != 1:
                    return 1
                grid[r][c] = 1  # backtrack

        # if not case 1 and 2, then case 3
        return 2
