class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"

        res = 0
        mask = 0  # mask is to count the occurrence of vowels
        mask_to_idx = {0: -1}  # "xxxx", when i points to the last index, length = 3 - (-1) = 4
        for i, c in enumerate(s):
            if c in vowels:
                # we use xor to keep it between even(0) or odd(1)
                mask = mask ^ (1 + ord(c) - ord('a'))  # +1, so that when char is a, 0 ^ 0 is handled
            if mask in mask_to_idx:
                length = i - mask_to_idx[mask]
                res = max(res, length)
            else:
                mask_to_idx[mask] = i
        return res
