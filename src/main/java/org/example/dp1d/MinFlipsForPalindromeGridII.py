from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total_flips = 0

        # Consider all 2x2 blocks
        for i in range((m + 1) // 2):
            for j in range((n + 1) // 2):
                # Coordinates of symmetric elements
                a = grid[i][j]
                b = grid[i][n - j - 1] if j < n - j - 1 else grid[i][j]
                c = grid[m - i - 1][j] if i < m - i - 1 else grid[i][j]
                d = grid[m - i - 1][n - j - 1] if (i < m - i - 1 and j < n - j - 1) else (
                    grid[i][j] if i == m - i - 1 and j == n - j - 1 else grid[m - i - 1][n - j - 1])

                # Count the number of 1s among the four symmetric cells
                ones_count = a + b + c + d

                # Minimum flips needed to make the block palindromic
                total_flips += min(ones_count, 4 - ones_count)

        return total_flips


# Example usage
solution = Solution()

# Example grid
grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Call the method and print the result
result = solution.minFlips(grid)
print(result)  # Output should be the minimal number of flips needed to make the grid palindromic
