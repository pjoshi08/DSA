class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        s = [s[i] for i in range(n)]
        for i in range(n - 1):
            a, b = int(s[i]), int(s[i + 1])
            if b < a and b % 2 == a % 2:
                tmp = s[i + 1]
                s[i + 1] = s[i]
                s[i] = tmp
                break

        return "".join(s)

obj = Solution()
s = "45320"
print(obj.getSmallestString(s))