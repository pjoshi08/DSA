from typing import List


# https://leetcode.com/problems/subarray-product-less-than-k/description/
class Solution:
    # Sliding window solution
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0

        l, r, count, prod = 0, 0, 0, 1
        n = len(nums)

        while r < n:
            prod *= nums[r]
            while prod >= k:
                prod //= nums[l]
                l += 1
            count += 1 + (r - l)
            r += 1
        return count
