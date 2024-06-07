from typing import List

# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                val = nums[i - 1] + 1
                ops += val - nums[i]
                nums[i] = val
        return ops
