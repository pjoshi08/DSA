from collections import Counter
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        best = -1
        dp = Counter()
        for n in nums:
            if n * n in dp:
                dp[n] = dp[n * n] + 1
            else:
                dp[n] = 1
            best = max(best, dp[n]) if dp[n] > 1 else best
        return best

    def longestSquareStreak(self, nums: List[int]) -> int:

        num_set = set(nums)
        nums.sort()
        longest = -1
        i = 0
        while i < len(nums):
            length = 0
            num = nums[i]
            while num in num_set:
                length += 1
                num *= num
            longest = max(longest, length) if length > 1 else longest
            i += 1
        return longest
