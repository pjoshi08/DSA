class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLen, tLen = len(s), len(t)
        if tLen > sLen: return ""

        sCount, tCount = {}, {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have, need = 0, len(tCount)
        # need = len(tCount) because it gives us the unique chars
        res = [-1, -1]  # to store [l, r] for window
        resLen = float('inf')
        l = 0
        for r in range(sLen):
            c = s[r]
            sCount[c] = 1 + sCount.get(c, 0)

            # check if for this char c we have reached the req freq
            if c in tCount and sCount[c] == tCount[c]:
                have += 1

            # check to see a possible solution
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # now we try to shorten the window to try to find a
                # better solution if it exists
                # first we reduce the freq of the leftmost char
                sCount[s[l]] -= 1

                # below check is similar to the check for 'have'
                # if we have decreased the req freq for this char
                # we reduce 'have'
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
