from collections import defaultdict
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        players = {}
        winners = set()
        for x, y in pick:
            if x not in players:
                players[x] = defaultdict(int)
            players[x][y] += 1
            if players[x][y] >= (x + 1):
                winners.add(x)
        return len(winners)