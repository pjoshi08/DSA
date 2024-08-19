from collections import Counter


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            zero = one = 0
            for j in range(i, n):
                if s[j] == '0':
                    zero += 1
                else:
                    one += 1

                if zero <= k or one <= k:
                    total += 1
        return total
