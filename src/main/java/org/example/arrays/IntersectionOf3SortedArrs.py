from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        count = {}
        for n in arr1:
            count[n] = 1 + count.get(n, 0)
        for n in arr2:
            count[n] = 1 + count.get(n, 0)
        for n in arr3:
            count[n] = 1 + count.get(n, 0)

        res = []
        for n, f in count.items():
            if f == 3:
                res.append(n)
        return res
