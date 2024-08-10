from typing import List


class Solution:
    # T: O(R * C), M: O(1)
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def magic(r, c):  # returns 1 for magic else 0
            # Ensure 1 - 9
            values = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] in values or not (0 < grid[i][j] < 10):
                        return 0
                    values.add(grid[i][j])

            # row sum
            for i in range(r, r + 3):
                if sum(grid[i][c:c + 3]) != 15:
                    return 0

            # col sum
            for i in range(c, c + 3):
                if grid[r][i] + grid[r + 1][i] + grid[r + 2][i] != 15:
                    return 0

            # diagonal sum
            if (
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15
            ):
                return 0
            return 1

        res = 0
        # only check for row, col positions from where a magic square can be made
        for r in range(ROWS - 2):
            for c in range(COLS - 2):
                res += magic(r, c)

        return res