class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        res = []
        for c in s:
            if c != " ":
                word += c
            elif word:
                res.append(word)
                word = ""
        if word:  # capture last word
            res.append(word)
        final = ""
        for i in range(len(res) - 1, -1, -1):  # iterate res in reverse
            final += res[i]
            if i > 0:
                final += " "
        return final