# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        for i in range(len(nums)):
            if ops % 2:
                nums[i] = 1 - nums[i]
            if nums[i] == 0:
                ops += 1

        return ops