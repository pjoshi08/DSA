from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dfs(i, s):
            if i == n:
                res.append(s)
                return

            dfs(i + 1, s + "1")
            if (i > 0 and s[i - 1] != "0") or i == 0:
                dfs(i + 1, s + "0")

        dfs(0, "")
        return res


obj = Solution()
print(obj.validStrings(3))
