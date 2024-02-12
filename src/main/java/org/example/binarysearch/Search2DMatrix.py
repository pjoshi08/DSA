from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        def search(nums):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    return True
            return False

        for r in range(ROWS):
            if target <= matrix[r][COLS - 1]:
                return search(matrix[r])


obj = Solution()
#matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
#target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
#matrix = [[1], [3]]
#target = 3
print(obj.searchMatrix(matrix, target))
