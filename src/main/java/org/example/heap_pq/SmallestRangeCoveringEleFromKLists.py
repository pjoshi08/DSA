import heapq
from typing import List


# 632. Smallest Range Covering Elements from K Lists
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left = right = nums[0][0]
        min_heap = []
        for i in range(k):  # find min and max nums for k lists
            l = nums[i]
            left = min(left, l[0])
            right = max(right, l[0])
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (num, list index, num index)

        res = [left, right]
        while True:
            num, listIdx, numIdx = heapq.heappop(min_heap)
            numIdx += 1
            if numIdx == len(nums[listIdx]):
                return res

            next_Num = nums[listIdx][numIdx]
            heapq.heappush(min_heap, (next_Num, listIdx, numIdx))
            right = max(right, next_Num)
            left = min_heap[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]
