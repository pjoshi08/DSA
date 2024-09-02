class Solution:
    def stringHash(self, s: str, k: int) -> str:
        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        n = len(s)
        i = 0
        subStrs = []
        while i < n:
            sub = s[i:i + k]
            subStrs.append(sub)
            i += k

        res = []
        for sub in subStrs:
            total = 0
            for c in sub:
                total += ord(c) - ord('a')
            res.append(chars[total % 26])

        return "".join(res)


obj = Solution()
s = "abcd"
k = 2
print(obj.stringHash(s, k))
