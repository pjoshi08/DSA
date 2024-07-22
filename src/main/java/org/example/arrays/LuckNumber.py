from typing import List


class Solution:
    # T: O(n + m), M = O(1)
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        rowMinMax = float('-inf')  # computing the max of the min row val
        for r in range(ROWS):
            rowMin = min(matrix[r])
            rowMinMax = max(rowMinMax, rowMin)

        colMaxMin = float('inf')  # computing the min of the max col val
        for c in range(COLS):
            colMax = max([matrix[r][c] for r in range(ROWS)])
            colMaxMin = min(colMaxMin, colMax)

        return [colMaxMin] if rowMinMax == colMaxMin else []

    # T: O(n * m), M = O(n + m), slower
    def luckyNumbers2(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        minNumsInRows = set()
        for r in range(ROWS):
            minNumsInRows.add(min(matrix[r]))

        maxNumsInCols = [0] * COLS
        for c in range(COLS):
            for r in range(ROWS):
                maxNumsInCols[c] = max(maxNumsInCols[c], matrix[r][c])

        maxNumsInCols = set(maxNumsInCols)

        for r in range(ROWS):
            for c in range(COLS):
                num = matrix[r][c]
                if num in minNumsInRows and num in maxNumsInCols:
                    return [num]
