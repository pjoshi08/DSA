from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k: return False

        nums.sort(reverse=True)
        dp = [0] * k
        target = total // k

        def dfs(i):
            if i == len(nums): return True

            for j in range(k):
                if dp[j] + nums[i] <= target:
                    dp[j] += nums[i]

                    if dfs(i + 1): return True

                    dp[j] -= nums[i]  # backtrack

                    if dp[j] == 0: break  # if this is true, we can never reach the solution from there
            return False

        return dfs(0)


obj = Solution()
# nums = [1, 2, 2, 2, 2]
# k = 3
# nums = [4,3,2,3,5,2,1]
# k = 4
# nums = [1, 2, 3, 4]
# k = 3
nums = [1, 1, 1, 1, 2, 2, 2, 2]
k = 4
print(obj.canPartitionKSubsets(nums, k))
