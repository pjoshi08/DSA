from typing import List

# https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        maxArea = 0
        heights = [0] * COLS
        for row in matrix:
            for c in range(COLS):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0

            stack = []
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    start = index
                    maxArea = max(maxArea, (i - index) * height)
                stack.append([start, h])
            for i, h in stack:
                maxArea = max(maxArea, (COLS - i) * h)
        return maxArea


obj = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalRectangle(matrix))