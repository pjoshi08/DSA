# 2083 Substrings That Begin and End With the Same Letter

class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = [0] * 26  # a ... z

        for c in s:
            # count occ of each char
            count[ord(c) - ord("a")] += 1

            # if we have seen a char before,
            res += count[ord(c) - ord("a")]
        return res

    # TLE, not valid, O(n^2)
    def numberOfSubstrings2(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    count += 1
        return count


obj = Solution()
# s = "abcba"
s = "abacad"
print(obj.numberOfSubstrings(s))
