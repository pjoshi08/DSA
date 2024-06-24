import collections
from typing import List


class Solution:
    # T: O(n), M: O(n)
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flipped = [False] * n
        validFlipFromLastWindow, count = 0, 0

        for i in range(n):
            if i >= k:
                # remove effect from last window
                if flipped[i - k]:
                    validFlipFromLastWindow -= 1
            # check if we need to flip, means 0
            if validFlipFromLastWindow % 2 == nums[i]:
                # check bound condition
                if i + k > n: return -1

                validFlipFromLastWindow += 1
                count += 1
                flipped[i] = True
        return count

    # T: O(n), M: O(k)
    def minKBitFlips2(self, nums: List[int], k: int) -> int:
        q = collections.deque()
        flipped, count = 0, 0
        n = len(nums)
        for i in range(n):
            if i >= k:
                flipped ^= q[0]  # remove effect from last window

            # if bit is 0
            if flipped == nums[i]:
                if i + k > n: return -1

                count += 1
                flipped ^= 1  # toggle
                q.append(1)
            else:
                q.append(0)

            if len(q) > k:
                q.popleft()

        return count

    # T: O(n), M: O(1)
    def minKBitFlips3(self, nums: List[int], k: int) -> int:
        flipsInPrevWindow, count = 0, 0
        n = len(nums)
        for i in range(n):
            # this condition changes based on input modification below
            if i >= k and nums[i - k] == 2:
                # nums[i - k] -= 2 # if interviewer doesn't allow to modify input
                flipsInPrevWindow -= 1
            # this condition determines if we want to flip
            if flipsInPrevWindow % 2 == nums[i]:
                # boundary condition
                if i + k > n:
                    return -1
                # mark bit flip
                nums[i] = 2  # can modify input?, if no nums[i] += 2
                count += 1
                flipsInPrevWindow += 1

        return count




