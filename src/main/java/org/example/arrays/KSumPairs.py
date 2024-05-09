from collections import defaultdict
from typing import List

# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numCount = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            n = k - nums[i]
            if n in numCount and numCount[n] > 0:
                count += 1
                numCount[n] -= 1
            else:
                numCount[nums[i]] += 1
        return count


obj = Solution()
nums = [3, 1, 3, 4, 3]
k = 6
print(obj.maxOperations(nums, k))
