import heapq
from typing import List


class Solution:
    # brute force soln, T: O(n^2logn), M: O(n^2)
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarr_sums = []
        mod = 10 ** 9 + 7
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum = (cur_sum + nums[j]) % mod
                subarr_sums.append(cur_sum)

        subarr_sums.sort()
        res = 0
        for i in range(left - 1, right):  # left and right are 1 indexed
            res = (res + subarr_sums[i]) % mod
        return res

    # minHeap solution, T: O(n^2logn), M: O(n)
    # Intuition: https://www.youtube.com/watch?v=7XTGlO6b16A
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10 ** 9 + 7
        minH = [(n, i) for i, n in enumerate(nums)]  # (num, index)
        heapq.heapify(minH)

        res = 0
        for i in range(right):  # this loop runs n^2 times
            num, index = heapq.heappop(minH)
            if i >= left - 1:
                res = (res + num) % mod
            if index + 1 < n:
                heapq.heappush(minH, (num + nums[index + 1], index + 1))
        return res