from typing import List

# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# Min Difference between smallest and largest in 3 moves
class Solution:
    # O(nlogn)
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4: return 0

        nums.sort()
        minDiff = float('inf')
        # there can be 4 scenarios to find the min diff:
        # 1. delete the 3 largest elements
        # 2. delete 1 smallest, 2 largest elements
        # 3. delete 2 smallest, 1 largest element
        # 4. delete 3 smallest elements
        for left in range(4):
            right = n - 4 + left
            minDiff = min(minDiff, nums[right] - nums[left])
        return minDiff