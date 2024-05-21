# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
class Solution:
    def originalDigits(self, s: str) -> str:
        digits = {
            'w': ('two', '2'),
            'u': ('four', '4'),
            'x': ('six', '6'),
            'f': ('five', '5'),
            'z': ('zero', '0'),
            'r': ('three', '3'),
            't': ('eight', '8'),
            's': ('seven', '7'),
            'i': ('nine', '9'),
            'n': ('one', '1')
        }

        # freq = Counter(s)
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)

        res = []
        for c, (word, num) in digits.items():
            # count = freq[c]
            count = freq.get(c, 0)
            res.append(num * count)
            if count != 0:
                for w in word: freq[w] -= count
        return "".join(sorted(res))

obj = Solution()
s = "owoztneoer"
#s = "fviefuro"
#s = "zerozero"
print(obj.originalDigits(s))
