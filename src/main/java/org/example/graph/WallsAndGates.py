import collections
from typing import List

# https://leetcode.com/problems/walls-and-gates/description/
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:  # queue wall coords
                    q.append((r, c))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            row, col = q.popleft()
            dist = rooms[row][col] + 1

            for dr, dc in dirs:
                r, c = row + dr, col + dc
                if r in (-1, ROWS) or c in (-1, COLS):  # boundary conditions
                    continue
                if dist < rooms[r][c]:  # no need to check if cell is a wall as dist > -1
                    rooms[r][c] = dist
                    q.append((r, c))


obj = Solution()
rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
obj.wallsAndGates(rooms)
