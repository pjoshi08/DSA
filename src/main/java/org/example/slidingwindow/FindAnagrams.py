from typing import List

# Find All Anagrams in a String: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        sCount, pCount = [0] * 26, [0] * 26
        for i in range(len(p)):
            pCount[ord(p[i]) - ord('a')] += 1

        window, l = len(p), 0
        res = []
        for r in range(len(s)):
            sCount[ord(s[r]) - ord('a')] += 1

            while (r - l + 1) > window:
                sCount[ord(s[l]) - ord('a')] -= 1
                l += 1
            if (r - l + 1) == window:
                equal = self.checkEquality(sCount, pCount)
                if equal: res.append(l)
        return res

    def checkEquality(self, sCount, pCount) -> bool:
        for i, n in enumerate(pCount):
            if n != sCount[i]: return False
        return True

obj = Solution()
#s = "cbaebabacd"
#p = "abc"
s = "abab"
p = "ab"
print(obj.findAnagrams(s, p))