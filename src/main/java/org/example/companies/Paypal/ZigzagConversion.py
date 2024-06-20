class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            # top down
            for j in range(numRows):
                if i < len(s):
                    rows[j].append(s[i])
                    i += 1

            # diagonal
            for j in range(numRows - 2, 0, -1):
                if i < len(s):
                    rows[j].append(s[i])
                    i += 1
        res = ""
        for r in rows:
            res += "".join(r)
        return res


obj = Solution()
s = "PAYPALISHIRING"
print(obj.convert(s, 4))
