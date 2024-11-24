from typing import List


class Solution:
    # O(n * k), O(n ^ 2) worst case
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

    # T: O(n), O(1)
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        consec_cnt = 1
        for r in range(len(nums)):
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                consec_cnt += 1

            while r - l + 1 > k:  # shift window if bigger
                # consec cnt would only have been inc if
                # this condition is true above, so we dec it here
                if nums[l] + 1 == nums[l + 1]:
                    consec_cnt -= 1
                l += 1

            if r - l + 1 == k:
                res.append(nums[r] if consec_cnt == k else -1)
        return res


nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
# nums = [4, 5]
# k = 1
obj = Solution()
print(obj.resultsArray(nums, k))
