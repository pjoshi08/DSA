from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countChars = [0] * 26  # a ... z
        for c in chars:
            countChars[ord(c) - ord('a')] += 1

        res = 0
        for word in words:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            isEqual = True
            for i in range(26):
                if count[i] > countChars[i]:
                    isEqual = False
                    break
            if isEqual:
                res += len(word)
        return res