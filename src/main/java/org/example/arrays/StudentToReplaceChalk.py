from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = 0
        n = len(chalk)
        for i in range(n):
            chalk_sum += chalk[i]
            if chalk_sum > k:
                break

        k = k % chalk_sum
        for i in range(n):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0
