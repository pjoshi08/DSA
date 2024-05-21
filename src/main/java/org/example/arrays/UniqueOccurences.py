from typing import List


# https://leetcode.com/problems/unique-number-of-occurrences/description/
class Solution:
    # Twice as better
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for n in arr:
            freq[n] = 1 + freq.get(n, 0)

        return len(freq) == len(set(freq.values()))

    def uniqueOccurrences2(self, arr: List[int]) -> bool:
        n = len(arr)
        if n == 1: return True
        numCount, freq = {}, set()

        for i in range(n):
            numCount[arr[i]] = 1 + numCount.get(arr[i], 0)

        for i in numCount.values():
            if i in freq: return False
            freq.add(i)
        return True


obj = Solution()
arr = [1, 2, 2, 1, 1, 3]
print(obj.uniqueOccurrences(arr))
