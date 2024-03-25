from typing import List


# Binary Watch: https://leetcode.com/problems/binary-watch/description/
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hr in range(12):
            for min in range(60):
                if bin(hr).count('1') + bin(min).count('1') == turnedOn:
                    res.append(f"{hr}:{min:02d}")
        return res
