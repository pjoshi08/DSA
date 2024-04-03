from typing import List


# https://leetcode.com/problems/unique-paths-iii/description/
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        start = None
        for r in range(ROWS):
            for c in range(COLS):
                count += grid[r][c] == 0
                if not start and grid[r][c] == 1:
                    start = (r, c)

        def backtrack(r, c):
            nonlocal count
            result = 0

            for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= dr < ROWS and 0 <= dc < COLS:
                    if grid[dr][dc] == 0:
                        grid[dr][dc] = -1
                        count -= 1
                        result += backtrack(dr, dc)
                        grid[dr][dc] = 0
                        count += 1
                    elif grid[dr][dc] == 2:
                        result += count == 0
            return result

        return backtrack(start[0], start[1])


obj = Solution()
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
print(obj.uniquePathsIII(grid))
