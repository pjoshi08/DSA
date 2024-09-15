from typing import List


# Remove duplicates from sorted array (in-place)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        insert = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:  # unique element
                nums[insert] = nums[i]
                insert += 1
        return insert
