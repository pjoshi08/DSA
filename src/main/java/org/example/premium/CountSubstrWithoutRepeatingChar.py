# You are given a string s consisting only of lowercase English letters. We call a substring
# special if it contains no character which has occurred at least twice (in other words, it
# does not contain a repeating character). Your task is to count the number of special substrings.
# For example, in the string "pop", the substring "po" is a special substring, however, "pop"
# is not special (since 'p' has occurred twice).
#
# Return the number of special substrings.
#
# A substring is a contiguous sequence of characters within a string. For example, "abc"
# is a substring of "abcd", but "acd" is not.

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        count, l = 0, 0
        freq = [0] * 26 # a...z

        for r in range(len(s)):
            freq[ord(s[r]) - ord("a")] += 1

            while freq[ord(s[r]) - ord("a")] > 1:
                freq[ord(s[l]) - ord("a")] -= 1
                l += 1
            count += r - l + 1

        return count


obj = Solution()
s = "abcd"
print(obj.numberOfSpecialSubstrings(s))
