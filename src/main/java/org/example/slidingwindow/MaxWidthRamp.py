from typing import List


# 962. Maximum Width Ramp
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        numLen = len(nums)
        max_right = [0] * numLen
        i = numLen - 1
        prev = 0

        for n in reversed(nums):
            max_right[i] = max(nums[i], prev)
            prev = max_right[i]
            i -= 1

        res = 0
        l = 0
        for r in range(numLen):
            while nums[l] > max_right[r]:
                l += 1
            res = max(res, r - l)
        return res
