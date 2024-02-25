class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1

        window, l = len(s1), 0
        for r in range(len(s2)):
            s2Count[ord(s2[r]) - ord('a')] += 1

            while (r - l + 1) > window:
                s2Count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if (r - l + 1) == window:
                equal = self.checkEquality(s1Count, s2Count)
                if equal: return True
        return False

    def checkEquality(self, s1Count, s2Count) -> bool:
        for i, n in enumerate(s1Count):
            if n != s2Count[i]: return False
        return True

obj = Solution()
s1 = "ab"
#s2 = "eidbaooo"
s2 = "eidboaoo"
print(obj.checkInclusion(s1, s2))