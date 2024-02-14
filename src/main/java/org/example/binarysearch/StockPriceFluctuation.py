from heapq import heappush
from heapq import heappop


# Stock Price Fluctuation: https://leetcode.com/problems/stock-price-fluctuation/description/
class StockPrice:

    def __init__(self):
        self.store = {}
        self.minH = []
        self.maxH = []
        self.curr = 0

    def update(self, timestamp: int, price: int) -> None:
        self.store[timestamp] = price
        if self.curr <= timestamp: self.curr = timestamp
        heappush(self.maxH, (-price, timestamp))
        heappush(self.minH, (price, timestamp))

    def current(self) -> int:
        return self.store[self.curr]

    def maximum(self) -> int:
        while self.store[self.maxH[0][1]] != -self.maxH[0][0]: heappop(self.maxH)
        return -self.maxH[0][0]

    def minimum(self) -> int:
        while self.store[self.minH[0][1]] != self.minH[0][0]: heappop(self.minH)
        return self.minH[0][0]
