from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1: return [nums[0]]

        if k == 1:
            return nums

        def isConsecutiveSorted(subarr):
            for i in range(1, len(subarr)):
                if subarr[i] != subarr[i - 1] + 1:
                    return False
            return True

        res = []
        for i in range(n - k + 1):
            subarr = nums[i:i + k]
            if isConsecutiveSorted(subarr):
                res.append(subarr[-1])
            else:
                res.append(-1)
        return res


nums = [1,2,3,4,3,2,5]
k = 3
# nums = [4, 5]
# k = 1
obj = Solution()
print(obj.resultsArray(nums, k))
