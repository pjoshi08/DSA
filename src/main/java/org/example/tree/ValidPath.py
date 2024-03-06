import collections
from typing import List


# Check if There is a Valid Path in a Grid: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])

        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        # rules for bidirectional transition, mapped to moves
        rules = {
            1: {LEFT: LEFT, RIGHT: RIGHT},  # meaning for street 1 we can move left to right or right to left
            2: {UP: UP, DOWN: DOWN},
            3: {UP: LEFT, RIGHT: DOWN},
            4: {UP: RIGHT, LEFT: DOWN},
            5: {DOWN: LEFT, RIGHT: UP},
            6: {DOWN: RIGHT, LEFT: UP}
        }

        q = collections.deque([(0, 0)])
        visited = {(0, 0)}
        while q:
            x, y = q.popleft()
            if x == ROWS - 1 and y == COLS - 1:
                return True
            for dx, dy in rules[grid[x][y]].values():
                nx, ny = x + dx, y + dy
                if (0 <= nx <= ROWS - 1 and 0 <= ny <= COLS - 1 and
                        (nx, ny) not in visited and (dx, dy) in rules[grid[nx][ny]]):
                    q.append((nx, ny))
                    visited.add((nx, ny))

        return False


obj = Solution()
grid = [[2, 4, 3], [6, 5, 2]]
print(obj.hasValidPath(grid))
