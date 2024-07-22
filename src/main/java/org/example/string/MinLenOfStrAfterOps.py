class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        x = 0
        freq = {}

        for c in s:
            freq[c] = 1 + freq.get(c, 0)

        for f in freq.values():
            # If f is odd, f - 1 chars can be removed
            # If f is even, f - 2 chars can be removed
            x += (f - 1) if (f % 2 == 1) else (f - 2)
        return n - x


obj = Solution()
s = "abaacbcbb"
print(obj.minimumLength(s))
