# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ops, i = 0, 0

        while i < n:
            if nums[i] == 0:
                if i <= n - 3:
                    nums[i] = 1 - nums[i]
                    nums[i + 1] = 1 - nums[i + 1]
                    nums[i + 2] = 1 - nums[i + 2]
                elif i == n - 2:
                    nums[i] = 1 - nums[i]
                    nums[i + 1] = 1 - nums[i + 1]
                    nums[i - 1] = 1 - nums[i - 1]
                elif i == n - 1:
                    nums[i] = 1 - nums[i]
                    nums[i - 1] = 1 - nums[i - 1]
                    nums[i - 2] = 1 - nums[i - 2]
                ops += 1
            i += 1

        if any(n == 0 for n in nums): return -1
        return ops