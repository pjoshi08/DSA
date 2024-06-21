from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        minForce = 0
        position.sort()

        # we do m-1 for high because we may place a ball at low
        # so we consider remaining balls to calculate high
        low, high = 1, int(position[-1] / (m - 1.0)) + 1
        while low < high:
            mid = low + (high - low) // 2

            if self.canPlaceBalls(position, mid, m):
                minForce = mid  # possible solution
                low = mid + 1  # discard left search space to find a better solution
            else:
                high = mid - 1  # discard right search space
        return minForce

    # x is the min force threshold
    def canPlaceBalls(self, position: List[int], x: int, m: int) -> bool:
        balls = 1
        prevPos = position[0]

        for pos in position[1:]:
            if pos - prevPos >= x:
                balls += 1
                prevPos = pos
            if balls == m:
                return True
        return False
