from typing import List


# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/submissions/1168272091/
class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        maxNum = 0
        maxDiff = 0

        for n in nums:
            res = max(res, maxDiff * n)
            maxDiff = max(maxDiff, maxNum - n)
            maxNum = max(maxNum, n)
        return res


    # O(n^3)
    def maximumTripletValue2(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            for j in range (i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res
