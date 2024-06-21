from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        curLargest = nums[-1]
        # No need to change the last element, already sorted
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= curLargest:
                curLargest = nums[i]
                continue

            if nums[i] % curLargest:
                numOfElements = nums[i] // curLargest + 1
                curLargest = nums[i] // numOfElements
            else:
                numOfElements = nums[i] // curLargest

            count += numOfElements - 1

        return count


obj = Solution()
# nums = [3,9,3]
# nums = [1,2,3,4,5]
nums = [12,9,7,6,17,19,21]
print(obj.minimumReplacement(nums))