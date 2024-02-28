from sys import maxsize
from typing import List

# Minimum Size Subarray Sum: https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = maxsize
        l = total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                size = min(size, r - l + 1)
                total -= nums[l]
                l += 1
        return size if size != maxsize else 0



obj = Solution()
nums = [2,3,1,2,4,3]
target = 7
#nums = [1,4,4]
#target = 4
#nums = [1,1,1,1,1,1,1,1]
#target = 11
print(obj.minSubArrayLen(target, nums))