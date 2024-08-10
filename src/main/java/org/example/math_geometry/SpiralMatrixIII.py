from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # directions for spiral order

        i, steps = 0, 1
        res = []
        r, c = rStart, cStart
        while len(res) < rows * cols:
            # 2 because the spiral goes right and then down
            # then it goes left and up
            for _ in range(2):
                dr, dc = directions[i]
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r, c = r + dr, c + dc
                i = (i + 1) % 4  # to keep it within bounds for directions
            steps += 1  # no of steps in spiral increases with each iteration
        return res


obj = Solution()
rows = 1
cols = 4
rStart = 0
cStart = 0
print(obj.spiralMatrixIII(rows, cols, rStart, cStart))