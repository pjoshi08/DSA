from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin_search(l, r, target):
            # find largest i, where nums[i] < target
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return r

        nums.sort()
        res = 0
        numLen = len(nums)
        for i in range(numLen):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (
                    bin_search(i + 1, numLen - 1, up + 1) -
                    bin_search(i + 1, numLen - 1, low)
            )
        return res
