from typing import List


class Solution:
    # T: O(n * m)
    def restoreMatrix2(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS, COLS = len(rowSum), len(colSum)

        matrix = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                # greedily pick the smaller of the two sums and assign value
                # at curr r, c
                matrix[r][c] = min(rowSum[r], colSum[c])
                # update sums
                rowSum[r] -= matrix[r][c]
                colSum[c] -= matrix[r][c]
        return matrix

    # T: O(n * m), time optimized
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS, COLS = len(rowSum), len(colSum)

        matrix = [[0] * COLS for _ in range(ROWS)]
        r, c = 0, 0
        while r < ROWS and c < COLS:
            matrix[r][c] = min(rowSum[r], colSum[c])
            rowSum[r] -= matrix[r][c]
            colSum[c] -= matrix[r][c]

            # at any point in time, we are picking the min of rowSum and colSum
            # meaning either rowSum[r] becomes 0 or colSum[c]
            # we increase index accordingly to optimize running time
            if rowSum[r] == 0:
                r += 1
            else:
                c += 1
        return matrix