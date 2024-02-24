
# Ugly Number II: https://leetcode.com/problems/ugly-number-ii/submissions/1183343138/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1: return 1
        ugls = [0] * n
        i1 = i2 = i3 = 0
        ugls[0] = 1
        for i in range(1, n):
            ugls[i] = min(ugls[i1] * 2, ugls[i2] * 3, ugls[i3] * 5)
            if ugls[i] == (ugls[i1] * 2): i1 += 1
            if ugls[i] == (ugls[i2] * 3): i2 += 1
            if ugls[i] == (ugls[i3] * 5): i3 += 1
        return ugls[n-1]