from typing import List


# Given an array of strings words, find the longest string in words such that every prefix of it is also in words.
#
# For example, let words = ["a", "app", "ap"]. The string "app" has prefixes "ap" and "a", all of which are in words.
# Return the string described above. If there is more than one string with the same length, return the
# lexicographically smallest one, and if no string exists, return "".
#
#
#
# Example 1:
#
# Input: words = ["k","ki","kir","kira", "kiran"]
# Output: "kiran"
# Explanation: "kiran" has prefixes "kira", "kir", "ki", and "k", and all of them appear in words.
# Example 2:
#
# Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: Both "apple" and "apply" have all their prefixes in words.
# However, "apple" is lexicographically smaller, so we return that.
# Example 3:
#
# Input: words = ["abc", "bc", "ab", "qwe"]
# Output: ""

class Solution:
    # O(n^2), 60%, check for better solution
    def longestWord(self, words: List[str]) -> str:
        words.sort(reverse=True)
        longest = 0
        res = ""
        wordSet = set(words)

        for w in words:
            allPrefixes = True
            for i in range(len(w)):
                if w[:i + 1] not in wordSet:
                    allPrefixes = False
                    break
            if allPrefixes and len(w) >= longest:
                longest = len(w)
                res = w
        return res
