# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = defaultdict(int)
        count = 0
        for t in time:
            if t % 60 == 0:
                count += freq[0]
            else:  # a % 60 + b % 60 == 60
                count += freq[60 - (t % 60)]
            freq[t % 60] += 1

        return count


obj = Solution()
time = [60, 60, 60]
print(obj.numPairsDivisibleBy60(time))
