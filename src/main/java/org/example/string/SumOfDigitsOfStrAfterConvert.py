class Solution:
    def getLucky(self, s: str, k: int) -> int:
        charToInt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                     'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                     'x': 24, 'y': 25, 'z': 26
                     }

        convert = []
        for c in s:
            convert.append(str(charToInt[c]))

        while k > 0:
            total = 0
            for conv in convert:
                for c in conv:
                    total += int(c)
            convert = [str(total)]
            k -= 1
        return int(convert[0])
