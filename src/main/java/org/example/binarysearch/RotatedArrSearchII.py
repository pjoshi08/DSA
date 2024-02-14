from typing import List

# Search in Rotated Sorted Array II: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution:

    # nums contains duplicates
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return True
            if nums[m] == nums[r]: r -= 1 # cannot determine which side is sorted
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return False
