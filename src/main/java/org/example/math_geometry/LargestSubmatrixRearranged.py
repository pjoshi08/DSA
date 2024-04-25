from typing import List


# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/
class Solution:
    # T = O(r * (c * log c)), M = O(log c) or O(c) (worst case) for sorting
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        # calculate height at each column
        for r in range(1, ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]

        res = 0
        # calculate max area
        for r in range(ROWS):
            matrix.sort()  # we can sort rows because we can rearrange columns

            for c in range(COLS):
                height = matrix[r][c]
                width = COLS - c  # len of row - current column index
                res = max(res, height * width)
        return res
