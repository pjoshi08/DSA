from typing import List


# Set mismatch: https://leetcode.com/problems/set-mismatch/description/
# Similar to LL Duplicate Number
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        copy = set()
        res = []

        for n in nums:
            if n in copy:
                res.append(n)
            copy.add(n)

        for i in range(1, len(nums) + 1):
            if i not in copy:
                res.append(i)
                return res
