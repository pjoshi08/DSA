# https://leetcode.com/problems/palindrome-permutation/description/
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = set()
        for c in s:
            if c not in chars:
                chars.add(c)
            else:
                chars.remove(c)
        return len(chars) <= 1


obj = Solution()
# s = "abcd"
# s = "aab"
s = "carerac"
print(obj.canPermutePalindrome(s))
