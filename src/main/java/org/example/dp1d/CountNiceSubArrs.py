# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
from typing import List


class Solution:
    # M = O(n), T = O(n), 95%
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        prefix = [0] * (n + 1)
        prefix[0] = 1
        s = 0
        for i in range(n):
            s += nums[i] % 2  # s only increases when num is odd
            if s >= k:
                res += prefix[s - k]
            prefix[s] += 1  # subarrs keep on increasing with i
        return res

    # Sliding window, M = O(1), T = O(n), 45%, slower
    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        # Num of subarr with exactly k odd nums =
        # num of subarr with at most k odd nums -
        # num of subarr with at most k - 1 odd nums
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k) -> int:
        s, j, res = 0, 0, 0
        for i in range(len(nums)):
            s += nums[i] % 2
            while s > k:
                # shrink window
                s -= nums[j] % 2
                j += 1
            res += (i - j + 1)
        return res