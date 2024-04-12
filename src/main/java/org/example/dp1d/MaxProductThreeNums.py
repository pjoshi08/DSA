from typing import List


# Medium: https://leetcode.com/problems/maximum-product-of-three-numbers/description/
# For this solution understand MaxProdSubarr solution
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        smallestTwo = [float('inf')] * 2
        largestThree = [float('-inf')] * 3

        for n in nums:
            if n <= smallestTwo[0]:
                smallestTwo[0] = n
                smallestTwo.sort(reverse=True)
            if n >= largestThree[0]:
                largestThree[0] = n
                largestThree.sort()
        # noinspection PyTypeChecker
        return max(smallestTwo[0] * smallestTwo[1] * largestThree[2],
                   largestThree[0] * largestThree[1] * largestThree[2])
