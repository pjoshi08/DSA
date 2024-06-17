from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # n ^ 0 = n
        for n in nums:
            res = n ^ res
        return res


obj = Solution()
#nums = [4, 1, 2, 1, 2]
nums = [4, 1]
print(obj.singleNumber(nums))
