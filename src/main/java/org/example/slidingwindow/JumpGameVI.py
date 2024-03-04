import collections
from typing import List


# Jump Game VI: https://leetcode.com/problems/jump-game-vi/description/
class Solution:

    # O(n) time, O(n) memory
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = collections.deque()
        q.append(0)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + dp[q[0]]  # max value in q within that window
            if q[0] < i - k + 1:  # maintains in bounds/window
                q.popleft()
            while q and dp[q[-1]] < dp[i]:  # Update q with current ith element
                q.pop()
            q.append(i)
        return dp[-1]

    # giving error for some cases, not final solution
    def maxResult2(self, nums: List[int], k: int) -> int:
        res = nums[0]
        l, r = 1, 1
        q = collections.deque()

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # pop leftVal from window if it's out of bounds
            while l > q[0]:
                q.popleft()

            if (r - l + 1) == k or r == len(nums) - 1:
                res += nums[q[0]]
                l = q[0] + 1
            r += 1

        return res


obj = Solution()
nums = [1, -1, -2, 4, -7, 3]
k = 2
# nums = [10,-5,-2,4,0,3]
# k = 3
# nums = [1,-5,-20,4,-1,3,-6,-3]
# k = 2
# nums = [100,-1,-100,-1,100]
# k = 2
print(obj.maxResult(nums, k))
