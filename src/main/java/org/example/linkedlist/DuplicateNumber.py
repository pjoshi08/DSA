from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0  # we start at 0 because 0 is never part of the cycle, values are between [1, n]
        while True:  # loop to find intersection
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:  # loop to find the start of LL cycle
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
