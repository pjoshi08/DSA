# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        countL, countR = 0, 0

        for c in s:
            if c == 'L': countL += 1
            if c == 'R': countR += 1

            if countL == countR: count += 1
        return count
