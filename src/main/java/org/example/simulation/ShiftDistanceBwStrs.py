from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        chars = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i',
                 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
                 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

        def movement_cost(c, target, dir):
            cost = 0
            while c != target:
                i = ord(c) - ord('a')
                cost += nextCost[i] if dir == 1 else previousCost[i]
                i = (i + dir) % 26
                c = chars[i]
            return cost

        total = 0
        for i, c in enumerate(s):
            total += min(
                movement_cost(c, t[i], 1),
                movement_cost(c, t[i], -1)
            )
        return total
