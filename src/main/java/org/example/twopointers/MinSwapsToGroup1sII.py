from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        total_ones = nums.count(1)
        max_window_ones = window_ones = 0
        l = 0
        for r in range(2 * N):  # 2N because the arr is circular, we simulate arr + arr
            if nums[r % N]:  # if nums[r] == 1, r % N as we need to keep in bounds
                window_ones += 1
            # cur window needs to be <= total_ones
            while r - l + 1 > total_ones:
                window_ones -= nums[l % N]  # nums[l] might be 0 or 1, we try to dec window
                l += 1
            max_window_ones = max(max_window_ones, window_ones)
        return total_ones - max_window_ones  # calc min swaps

    