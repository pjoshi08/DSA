from typing import List


# Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/description/
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        subStr = list(s)

        def dfs(i):
            nonlocal subStr
            if i >= len(s):
                res.append(''.join(subStr.copy()))
                return

            c = subStr[i]
            if c.isalpha():
                # Decision to do uppercase
                subStr[i] = c.upper()
                dfs(i + 1)

                # Decision to not do uppercase
                subStr[i] = c.lower()
                dfs(i + 1)
            else:
                dfs(i + 1)

        dfs(0)
        return res


obj = Solution()
s = "a1b2"
print(obj.letterCasePermutation(s))
