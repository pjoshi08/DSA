import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        res, minH = [], []
        for key, val in freq.items():
            heapq.heappush(minH, (-val, key))
        while k > 0:
            k -= 1
            # v, key = heapq.heappop(minH)
            res.append(heapq.heappop(minH)[-1])
        return res


obj = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(obj.topKFrequent(nums, k))