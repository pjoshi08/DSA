from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def is_palindrome(arr):
            return arr == arr[::-1]

        def min_flips_needed(arr):
            return sum(1 for i in range(len(arr) // 2) if arr[i] != arr[-i-1])

        # Calculate minimum flips for rows
        min_flips_row = sum(min_flips_needed(row) for row in grid if not is_palindrome(row))

        # Calculate minimum flips for columns
        min_flips_col = 0
        for c in range(m):
            col = [grid[r][c] for r in range(n)]
            if not is_palindrome(col):
                min_flips_col += min_flips_needed(col)

        return min(min_flips_row, min_flips_col)


# Example usage
# grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
grid = [[1],[0]]
solution = Solution()
print(solution.minFlips(grid))  # Output: 2
