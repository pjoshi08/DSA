class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        sMap = {}
        for c in s:
            sMap[c] = sMap.get(c, 0) + 1
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        for c in s:
            if sMap[c] != tMap.get(c, 0):
                return False
        return True
