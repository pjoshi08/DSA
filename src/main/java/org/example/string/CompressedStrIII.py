class Solution:
    def compressedString(self, word: str) -> str:
        count = {}
        comp = []
        wordLen = len(word)
        i = 0
        while i < wordLen:
            c = word[i]
            count[c] = 1 + count.get(c, 0)
            while (i + 1 < wordLen and word[i + 1] == c and
                   count[c] < 9):
                i += 1
                count[c] += 1

            comp.append(str(count[c]) + c)
            count[c] = 0
            i += 1

        return "".join(comp)
