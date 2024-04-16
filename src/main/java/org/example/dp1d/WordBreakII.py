from collections import defaultdict
from typing import List


# https://leetcode.com/problems/word-break-ii/description/
class Solution:
    # Slower solution, faster solution is TrieNode
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wCount = defaultdict(int)
        for w in wordDict:
            wCount[w] = 1

        def wordsEndingIn(i):
            if i == len(s):
                return ['']
            res = []
            for j in range(i + 1, len(s) + 1):
                # if s[i:j] in wordDict:
                if wCount[s[i:j]]:
                    for tail in wordsEndingIn(j):
                        if tail:
                            res.append(s[i:j] + ' ' + tail)
                        else:
                            res.append(s[i:j])
            return res

        return wordsEndingIn(0)


obj = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(obj.wordBreak(s, wordDict))
