from typing import List


# Score After Flipping Matrix
# https://leetcode.com/problems/score-after-flipping-matrix/description/
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # to flip row, check if the most significant bit is 0
        # then we flip otherwise not
        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS): grid[r][c] ^= 1  # flip

        # for column, we count num of 1s and 0s
        # if count[0] > count[1], we flip column
        for c in range(COLS):
            count = sum(grid[r][c] for r in range(ROWS))
            if count < ROWS - count:  # this means there are more 0s in the column
                for r in range(ROWS): grid[r][c] ^= 1

        return sum(int("".join(map(str, grid[r])), 2) for r in range(ROWS))
