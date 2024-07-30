import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    # T: O(logn), Binary search
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        l, r = 0, len(self.prefix_sums)
        while l < r:
            mid = l + (r - l) // 2
            if target > self.prefix_sums[mid]:
                l = mid + 1
            else:
                r = mid
        return l

    # T: O(n), linear search
    def pickIndex2(self) -> int:
        target = self.total_sum * random.random()
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
