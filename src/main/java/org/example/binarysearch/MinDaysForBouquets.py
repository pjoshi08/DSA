from typing import List


# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1

        start, end = 0, max(bloomDay)
        minDays = -1

        while start <= end:
            midDay = (start + end) // 2

            if self.numOfbouquets(bloomDay, midDay, k) >= m:
                minDays = midDay
                end = midDay - 1
            else:
                start = midDay + 1
        return minDays

    def numOfbouquets(self, bloomDay: List[int], midDay: int, k: int):
        count, bouquets = 0, 0

        for day in bloomDay:
            if day <= midDay:
                count += 1
            else:  # breaks adjacency, reset count
                count = 0

            if count == k:
                bouquets += 1
                count = 0

        return bouquets
