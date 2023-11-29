import heapq


class MedianFinder(object):

    def __init__(self):
        # two heaps, small - minheap, large - maxheap
        # heaps should be roughly equal size
        self.small, self.large = [], []

    def addNum(self, num):
        heapq.heappush(self.small, -1 * num)
        # make sure every small num is <= every large num
        if (self.small and self.large and
                (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # check for uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(3)
param_3 = obj.findMedian()
print(param_3)