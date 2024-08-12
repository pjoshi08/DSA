import heapq
from collections import defaultdict
from typing import List


class MedianFinder:

    def __init__(self):
        # small = maxHeap, large = minHeap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # first push in small
        heapq.heappush(self.small, -num)

        # check if all elements in small < all elements in large
        if self.large and -self.small[0] > self.large[0]:
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)

        # Check if length of both heaps is not greater than 1 from each other
        if len(self.small) > len(self.large) + 1:
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)
        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2  # return decimal division
