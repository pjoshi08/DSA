from typing import List


class Solution:
    # Two pointer solution, O(n)
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        bits = [0] * 32

        def update_bits(n, diff):  # diff to set or unset the bit
            for i in range(32):
                if n & (1 << i):  # to check if ith bit is set
                    bits[i] += diff

        def bits_to_int():
            num = 0
            for i in range(32):
                if bits[i]:  # if ith bit is set
                    num += (1 << i)
            return num

        l = 0
        for r in range(len(nums)):
            update_bits(nums[r], 1)  # add nums[r] to bits
            cur_or = bits_to_int()

            while l <= r and cur_or >= k:
                res = min(res, r - l + 1)
                update_bits(nums[l], -1)  # remove nums[l] from bits
                cur_or = bits_to_int()
                l += 1

        return -1 if res == float('inf') else res
