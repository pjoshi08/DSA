import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1) # count 1s

        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                dp[i] = 1 + dp[i + 1]
            else:
                dp[i] = dp[i + 1]
        ops = 0
        for i in range(n):
            if nums[i] == 0:
                ops = 1 + dp[i + 1]
                break

        return ops


obj = Solution()
# nums = [0,1,1,0,1]
nums = [0, 1, 0, 0, 1]
k = 2
print(obj.minOperations(nums))