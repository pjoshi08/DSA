import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:

            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in (-1, ROWS) or c in (-1, COLS) or
                            grid[r][c] != 1):
                        continue
                    grid[r][c] = 2
                    q.append([r, c])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
