from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []

        def dfs(i):
            if i >= len(nums):
                res.append(subSet.copy())
                return

            # Decision to include the number in the subset
            subSet.append(nums[i])
            dfs(i + 1)

            # Decision to exclude the number from the subset
            subSet.pop()
            dfs(i + 1)

        dfs(0)
        return res
