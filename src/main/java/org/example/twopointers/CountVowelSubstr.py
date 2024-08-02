from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        freq = {}
        count = 0
        for i, c in enumerate(word):
            if c in vowels:
                if not i or word[i - 1] not in vowels:  # if i == 0 or prev char is not vowel, reset pointers
                    l = r = i
                    freq.clear()
                freq[c] = 1 + freq.get(c, 0)
                while len(freq) == 5 and all(freq.values()):  # if all freq.values() >= 1, win condition
                    freq[word[r]] -= 1
                    r += 1  # we try to expand window till win condition is still satisfied
                count += r - l
        return count