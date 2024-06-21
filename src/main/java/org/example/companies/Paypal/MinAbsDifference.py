from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float('inf')
        arr.sort()
        res = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < minDiff:
                minDiff = diff
                res = []
            if diff == minDiff:
                res.append([arr[i - 1], arr[i]])
        return res


