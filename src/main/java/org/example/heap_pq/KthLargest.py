import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1
        return -heapq.heappop(nums)


obj = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(obj.findKthLargest(nums, k))
