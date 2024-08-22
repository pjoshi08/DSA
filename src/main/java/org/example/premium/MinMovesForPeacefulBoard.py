from typing import List


# Given a 2D array rooks of length n, where rooks[i] = [xi, yi] indicates the
# position of a rook on an n x n chess board. Your task is to move the rooks
# 1 cell at a time vertically or horizontally (to an adjacent cell) such that
# the board becomes peaceful.
#
# A board is peaceful if there is exactly one rook in each row and each column.
#
# Return the minimum number of moves required to get a peaceful board.
#
# Note that at no point can there be two rooks in the same cell.
class Solution:
    # T: O(n), M: O(n)
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        row = [0] * n
        col = [0] * n
        for x, y in rooks:
            row[x] += 1
            col[y] += 1

        min_moves = 0
        row_min_moves, col_min_moves = 0, 0
        for i in range(n):
            row_min_moves += row[i] - 1
            col_min_moves += col[i] - 1

            min_moves += abs(row_min_moves) + abs(col_min_moves)

        return min_moves
