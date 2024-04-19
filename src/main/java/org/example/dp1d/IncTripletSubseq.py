import math
from typing import List

# https://leetcode.com/problems/increasing-triplet-subsequence/description/
class Solution:
    # T = O(n), M = O(1)
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n  # this means n > first
            else:
                return True  # first < second < n as both the above conditions are false
        return False

    # maintain maxSoFar and minSoFar, T = O(n), M = O(n)
    def increasingTriplet3(self, nums: List[int]) -> bool:
        n = len(nums)
        maxSoFar = [0] * n
        maxSoFar[-1] = nums[-1]
        for i in reversed(range(n - 2)):
            maxSoFar[i] = max(maxSoFar[i + 1], nums[i + 1])

        minSoFar = nums[0]
        for i in range(1, n - 1):
            if minSoFar < nums[i] < maxSoFar[i]:
                return True
            minSoFar = min(minSoFar, nums[i])
        return False

    # TLE
    def increasingTriplet2(self, nums: List[int]) -> bool:
        LIS = [1] * (len(nums) + 1)

        for i in reversed(range(len(nums) - 1)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                if LIS[i] == 3: return True
        return False
