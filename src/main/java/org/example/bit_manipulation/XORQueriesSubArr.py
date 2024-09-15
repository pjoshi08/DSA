from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for n in arr:
            prefix.append(prefix[-1] ^ n)

        res = []
        for left, right in queries:
            res.append(
                prefix[right + 1] ^ prefix[left]
            )
        return res

    # Without extra space
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        res = []
        for left, right in queries:
            total = arr[right]
            remove = 0 if left == 0 else arr[left - 1]
            res.append(total ^ remove)
        return res
