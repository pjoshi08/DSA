from typing import List


class Solution:
    # One pass solution
    def longestSubarray(self, nums: List[int]) -> int:
        # Case 1: n < cur_max, n & cur_max < cur_max
        # Case 2: n == cur_max, n & cur_max == cur_max
        # Case 3: n > cur_max, n & cur_max < cur_max

        res, size = 0, 0
        cur_max = 0
        for n in nums:
            if n > cur_max:
                cur_max = n
                size = 1
                res = 0  # reset res for the case [2,2,2,2,3,3]
            elif n == cur_max:
                size += 1
            else:  # n < cur_max
                size = 0
            res = max(res, size)
        return res

    # Two pass solution
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        res, size = 0, 0
        for n in nums:
            if n == target:
                size += 1
            else:
                size = 0
            res = max(res, size)
        return res
