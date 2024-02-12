from typing import List

# Maximum Candies allocated to k children: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies): return 0
        l, r = 1, max(candies)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            piles = 0
            for c in candies:
                piles += (c // mid)

            if piles >= k:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res


obj = Solution()
#candies = [5,8,6]
#k = 3
candies = [4,7,5]
k = 4
print(obj.maximumCandies(candies, k))