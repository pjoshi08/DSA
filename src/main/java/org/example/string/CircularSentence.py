class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        wordsLen = len(words)
        i, j = 0, 1
        isCircular = True
        while j < wordsLen:
            if words[i][-1] != words[j][0]:
                isCircular = False
                break
            i += 1
            j += 1

        first, last = words[0], words[wordsLen - 1]
        return isCircular and first[0] == last[-1]