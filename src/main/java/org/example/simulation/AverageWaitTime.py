from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        start, end = 0, 0

        for c in customers:
            if time == 0 or c[0] > end:  # first customer or if the customer arrives when chef is free
                start = c[0]
            else:
                start = end

            end = start + c[1]
            time += end - c[0]

        return time / len(customers)


    def averageWaitingTime2(self, customers: List[List[int]]) -> float:
        time = 0
        start, end = 0, 0

        for c in customers:
            start = max(end, c[0]) # first customer or if the customer arrives when chef is free
            end = start + c[1]
            time += end - c[0]

        return time / len(customers)