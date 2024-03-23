from typing import List


# Combinations: https://leetcode.com/problems/combinations/description/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(remain, cur, start):
            if remain == 0:
                res.append(cur.copy())
            else:
                for i in range(start, n + 1):
                    cur.append(i)
                    backtrack(remain - 1, cur, i + 1)
                    cur.pop()

        backtrack(k, [], 1)
        return res


obj = Solution()
n, k = 4, 2
print(obj.combine(n, k))
