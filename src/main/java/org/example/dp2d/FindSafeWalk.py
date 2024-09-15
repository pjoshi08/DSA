from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        cache = {}  # (i, j) -> T/F

        def dfs(r, c, h):
            if r == ROWS - 1 and c == COLS - 1 and h >= 1:
                return True
            elif r == ROWS - 1 and c == COLS - 1 and h < 1:
                return False
            if (r, c) in cache: return cache[(r, c)]
            if (r in (-1, ROWS) or c in (-1, COLS) or
                    h < 1 or (r, c) in visit):
                return False

            visit.add((r, c))
            h = h - grid[r][c]
            res = (dfs(r + 1, c, h) or
                   dfs(r - 1, c, h) or
                   dfs(r, c + 1, h) or
                   dfs(r, c - 1, h))
            cache[(r, c)] = res
            return res

        visit = set()
        return dfs(0, 0, health)


obj = Solution()
grid = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
health = 1
print(obj.findSafeWalk(grid, health))
