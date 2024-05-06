from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r in (-1, ROWS) or c in (-1, COLS) or
                    board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. Reverse thinking: capture un-surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and
                        (r in (0, ROWS - 1) or c in (0, COLS - 1))):
                    capture(r, c)

        # 2. Capture surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. Recover un-surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
