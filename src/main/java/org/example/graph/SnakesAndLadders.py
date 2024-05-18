import collections
from typing import List


# https://leetcode.com/problems/snakes-and-ladders/description/
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:  # odd row has reverse direction for board
                c = length - 1 - c
            return [r, c]

        q = collections.deque()
        q.append([1, 0])  # [square, moves]
        visit = set()
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:  # snake or ladder, move to that pos
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1
