class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        sLen = len(s)
        for i, c in enumerate(s):
            if (res and res[-1] == c and i + 1 < sLen and
                    s[i + 1] == c):
                continue
            else:
                res.append(c)
        return "".join(res)
