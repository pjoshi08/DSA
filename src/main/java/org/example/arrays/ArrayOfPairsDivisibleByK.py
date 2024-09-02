import math
from collections import Counter
from typing import List


class Solution:
    # Similar to two sum, store gcds and work through multiples of k
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = Counter()
        res = 0
        n = len(nums)

        for i in range(n):
            x = math.gcd(k, nums[i])  # if k = 10, nums[i] = 12, gcd = 2
            want = k // x  # in that case, k / 2 = 5 (want)
            for num in counter:
                if num % want == 0:  # if we find a num in multiples of `want`, we increase by its count
                    res += counter[num]
            counter[x] += 1  # but we count gcds to use against multiples of k (want)
        return res
