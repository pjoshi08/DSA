import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:  # first = -8, second = -7
                heapq.heappush(stones, first - second)  # -8 - (-7) = -1

        stones.append(0)
        return abs(stones[0])