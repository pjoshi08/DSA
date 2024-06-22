# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for n in nums:
            if n % 3 != 0:
                count += 1
        return count
