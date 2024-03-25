from typing import List


# Maximum Strong Pair XOR I: https://leetcode.com/problems/maximum-strong-pair-xor-i/description/
class Solution:
    # O(n^2) but beats 95%, sliding window solution
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0
        nums.sort()

        while r < len(nums):
            x = nums[l]
            y = nums[r]
            if y - x > x:
                l += 1
                continue

            for i in range(l, r):
                res = max(res, nums[i] ^ y)
            r += 1
        return res

    def maximumStrongPairXor3(self, nums: List[int]) -> int:
        res = 0

        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    res = max(res, x ^ y)
        return res

    def maximumStrongPairXor2(self, nums: List[int]) -> int:
        pairs = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    pairs.append((nums[i], nums[j]))

        maxVal = 0
        for pair in pairs:
            first, second = pair
            maxVal = max(maxVal, first ^ second)
        return maxVal


obj = Solution()
nums = [1, 2, 3, 4, 5]
print(obj.maximumStrongPairXor(nums))
