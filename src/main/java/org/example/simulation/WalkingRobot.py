from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # N, E, S, W, order is important
        d = 0
        res = 0
        obstacles = {tuple(o) for o in obstacles}

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]
                for _ in range(c):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy

            res = max(res, x ** 2 + y ** 2)
        return res
