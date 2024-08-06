from typing import List


class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.grid = grid
        self.adj_dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.diag_dirs = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        self.coordinates = {}
        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.coordinates[self.grid[r][c]] = [r, c]

    def adjacentSum(self, value: int) -> int:
        return self.calc_sum(value, self.adj_dirs)

    def diagonalSum(self, value: int) -> int:
        return self.calc_sum(value, self.diag_dirs)

    def calc_sum(self, value, dirs):
        r, c = self.coordinates[value]
        diag_sum = 0
        for dr, dc in dirs:
            row, col = r + dr, c + dc
            if row in (-1, self.ROWS) or col in (-1, self.COLS): continue
            diag_sum += self.grid[row][col]
        return diag_sum


# Your neighborSum object will be instantiated and called as such:
grid = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]
obj = neighborSum(grid)
print(obj.adjacentSum(1))
print(obj.diagonalSum(4))
print(obj.diagonalSum(4))
print(obj.diagonalSum(8))
