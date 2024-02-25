from typing import List


# Max Consecutives III: https://leetcode.com/problems/max-consecutive-ones-iii/description/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        res = l = maxf = 0
        for r in range(len(nums)):
            if nums[r] == 1: count += 1
            maxf = max(maxf, count)

            while (r - l + 1) - maxf > k:
                if nums[l] == 1: count -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


obj = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 2
# k = 3
print(obj.longestOnes(nums, k))
