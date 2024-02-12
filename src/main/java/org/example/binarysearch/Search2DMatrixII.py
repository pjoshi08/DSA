from typing import List

# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = ROWS - 1, 0
        while r >= 0 and c < COLS:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False



obj = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 50
print(obj.searchMatrix(matrix, target))
