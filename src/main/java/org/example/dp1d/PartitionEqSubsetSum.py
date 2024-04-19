from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        dp = set()
        dp.add(0)
        target = total // 2

        for i in reversed(range(len(nums))):
            nextSet = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextSet.add(t + nums[i])
                nextSet.add(t)
            dp = nextSet
        return False
