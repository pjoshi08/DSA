from collections import deque
from typing import List, Optional

from org.example.linkedlist.ListNode import ListNode

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()  # [(r, c)]
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if (r in (-1, ROWS) or c in (-1, COLS) or
                            grid[r][c] != 1):
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c))
            time += 1
        return time if fresh == 0 else -1


obj = Solution()
grid = [[0, 1]]
print(obj.orangesRotting(grid))