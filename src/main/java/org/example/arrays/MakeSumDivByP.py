from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        res = len(nums)  # we have to minimize this and we cannot remove the whole arr
        remainder_to_idx = {
            0: -1  # for the case when first element is the remainder to remove
        }
        cur_sum = 0
        for i, n in enumerate(nums):
            # x = cur_sum - remainder, we have to remove x
            cur_sum = (cur_sum + n) % p  # mod p coz we only care about the remainder to remove
            prefix = (cur_sum - remainder + p) % p  # add & mod by p so as to keep it +ve and within bounds
            if prefix in remainder_to_idx:
                length = i - remainder_to_idx[prefix]
                res = min(res, length)
            remainder_to_idx[cur_sum] = i
        return -1 if res == len(nums) else res
