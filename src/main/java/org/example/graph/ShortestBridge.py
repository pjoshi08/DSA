from collections import deque
from typing import List


# https://leetcode.com/problems/shortest-bridge/description/
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def invalid(r, c):
            return r in (-1, N) or c in (-1, N)

        visit = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c]
                    or (r, c) in visit):
                return

            visit.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]: return res
                        visit.add((curR, curC))
                        q.append((curR, curC))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
