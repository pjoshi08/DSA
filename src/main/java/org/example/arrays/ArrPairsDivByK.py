from collections import Counter
from typing import List

# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = Counter(v % k for v in arr)  # we just need the last digit to check for divisibility by k

        for key in freq.keys():
            # key will be between 0 and k - 1
            other_key = (k - key) % k  # mod k for key = 0 case

            if key == other_key:
                if freq[key] % 2 != 0:
                    return False
            else:  # key != other_key
                if freq[key] != freq[other_key]:
                    return False
        return True
