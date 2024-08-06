from typing import List


class Solution:
    # T: O(nlogn), M: O(n)
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # Based on the requests, we count the number of times an index occurs in the requests
        count = [0] * (len(nums) + 1)
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        res, mod = 0, 10 ** 9 + 7
        nums.sort(reverse=True)
        count.sort(reverse=True)
        # Formula is, we multiply the max num based on the num of times an index is requested
        # [5, 4, 3, 2, 1] * [2, 1, 1, 1, 0]
        for n, c in zip(nums, count):
            # even though len(count) > len(nums), loop won't execute after we reach the end of nums
            res += n * c
        return res % mod
