from typing import List


class Solution:
    # Brute force, O(n^2)
    def canSortArray(self, nums: List[int]) -> bool:
        numLen = len(nums)
        for i in range(numLen):
            flag = False
            for j in range(numLen - i - 1):
                if nums[j] <= nums[j + 1]:
                    continue
                if bin(nums[j]).count("1") == bin(nums[j + 1]).count("1"):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
                else:
                    return False
                if not flag:
                    break
        return True
