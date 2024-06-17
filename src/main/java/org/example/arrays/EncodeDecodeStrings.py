from typing import List


# Design an algorithm to encode a list of strings to a string. The encoded string is then sent
# over the network and is decoded back to the original list of strings.
#
# Define a strategy to encode a list of strings to a string and then decode the string back to the original list
# https://leetcode.com/problems/encode-and-decode-strings/description/

class Codec:
    def encode(self, strs: List[str]) -> str:
        # strategy: len(s) + # + s
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # identify number, calc len, update indices
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            end = j + length + 1
            res.append(s[j + 1:end])
            i = end
        return res


# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ["Hello", "World"]
print(codec.decode(codec.encode(strs)))
