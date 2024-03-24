from typing import List


class Solution:
    # This solution is better on Leetcode
    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(pos, cur, target):
            if target == 0:
                res.append(cur[:])
                return
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(i + 1, cur, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res


obj = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(obj.combinationSum2(candidates, target))
