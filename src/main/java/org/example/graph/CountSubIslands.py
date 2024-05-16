from typing import List

# https://leetcode.com/problems/count-sub-islands/
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()

        def dfs(r, c):
            if (r in (-1, ROWS) or c in (-1, COLS)
                    or grid2[r][c] == 0 or (r, c) in visit):
                return True  # just means we reached grid2 island boundary, grid2 island allowed to be shorter

            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:  # this means grid2[r][c] is 1
                res = False

            res = dfs(r + 1, c) and res
            res = dfs(r - 1, c) and res
            res = dfs(r, c - 1) and res
            res = dfs(r, c + 1) and res
            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                    count += 1
        return count
