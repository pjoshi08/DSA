from functools import reduce
from itertools import combinations, accumulate
from typing import List

# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
class Solution:
    def subsetXORSum2(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) + 1):
            for arr in combinations(nums, i):
                res += list(accumulate(arr, func=lambda x, y: x ^ y))[-1]
        return res

    def subsetXORSum(self, nums: List[int]) -> int:
        res = [0]

        def backtrack(i, cur):
            if i >= len(nums):
                if len(cur) == 1:
                    res[0] += cur[0]
                elif cur:
                    res[0] += reduce(lambda x, y: x ^ y, cur)
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)

            cur.pop()
            backtrack(i + 1, cur)

        backtrack(0, [])

        return res[0]


obj = Solution()
# nums = [1, 3]
# nums = [5,1,6]
nums = [3, 4, 5, 6, 7, 8]
print(obj.subsetXORSum(nums))
