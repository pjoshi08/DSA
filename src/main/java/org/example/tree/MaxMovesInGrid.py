from collections import deque
from typing import List

# 2684. Maximum Number of Moves in a Grid
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dirs = [-1, 0, 1]  # row directions
        ROWS, COLS = len(grid), len(grid[0])
        visit = [[False] * COLS for _ in range(ROWS)]
        q = deque()

        for r in range(ROWS):
            visit[r][0] = True
            q.append((r, 0, 0))

        moves = 0
        while q:
            for _ in range(len(q)):
                r, c, count = q.popleft()

                moves = max(moves, count)

                for dr in dirs:
                    row, col = r + dr, c + 1  # will always move 1 col to the right

                    if (0 <= row < ROWS and
                            0 <= col < COLS and
                            not visit[row][col] and
                            grid[row][col] > grid[r][c]):
                        visit[row][col] = True
                        q.append((row, col, count + 1))

        return moves