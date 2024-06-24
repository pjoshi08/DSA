import heapq
from typing import List


class Solution:
    # Sliding window
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1: return 1

        maxH, minH = [], []  # (val, index)
        left, maxSize = 0, 0
        for right in range(len(nums)):
            heapq.heappush(maxH, (-nums[right], right))
            heapq.heappush(minH, (nums[right], right))

            while -maxH[0][0] - minH[0][0] > limit:
                # update left to remove invalid num which will be the
                # leftmost index of invalid num
                left = min(maxH[0][1], minH[0][1]) + 1

                # pop invalid entries
                while maxH[0][1] < left:
                    heapq.heappop(maxH)
                while minH[0][1] < left:
                    heapq.heappop(minH)
            maxSize = max(maxSize, right - left + 1)
        return maxSize
