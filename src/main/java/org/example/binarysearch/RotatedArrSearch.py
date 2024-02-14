from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 1 if target == nums[0] else -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m

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
        return -1


obj = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
#target = 3
#nums = [1]
#target = 0
#nums = [5,1,3]
#target = 3
print(obj.search(nums, target))