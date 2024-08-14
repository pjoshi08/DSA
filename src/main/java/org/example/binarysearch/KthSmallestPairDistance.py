from typing import List


# https://www.youtube.com/watch?v=bQ-QcFKwsZc
class Solution:
    # Intuition: generating all pairs will take O(n^2) and then
    # finding the diff of each pair and sorting it will also take
    # O(n logn). We actually do not need to do that.
    # We can think of it as our ans will lie in the search space
    # [0, max(nums)] We can then do binary search on this input
    # space and try to count the num of pairs that have diff <= m
    # we do that counting of pairs by sliding window
    # T: O(nlogn + nlog max), nlogn for sorting,
    # sliding window -> n, binary search -> log max
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        # sliding window
        def helper(dist) -> int:
            # count pairs that have
            # diff <= dist
            l = 0
            res = 0
            for r in range(n):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l
            return res

        l, r = 0, nums[-1]
        while l < r:  # we stop when l == r, that will be the solution
            m = l + (r - l) // 2
            pairs = helper(m)
            if pairs >= k:  # this means m could be a possible solution
                # hence we do not eliminate m
                r = m
            else:  # this means pairs < k, we can eliminate m
                l = m + 1

        return r
