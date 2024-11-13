from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_strictly_increasing(start: int, length: int) -> bool:
            for i in range(start, start + length - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for i in range(len(nums) - 2 * k + 1):
            if is_strictly_increasing(i, k):
                if is_strictly_increasing(i + k, k):
                    return True

        return False
