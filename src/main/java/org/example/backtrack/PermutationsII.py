from collections import Counter
from typing import List


# Permutations II: https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for key in count:
                if count[key]:
                    count[key] -= 1
                    backtrack(cur + [key])
                    count[key] += 1

        backtrack([])
        return res


obj = Solution()
nums = [1, 1, 2]
print(obj.permuteUnique(nums))
