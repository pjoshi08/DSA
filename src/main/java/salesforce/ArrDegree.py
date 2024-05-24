from collections import Counter
from typing import List


# https://leetcode.com/problems/degree-of-an-array/description/
class Solution:
    # beats 75%, leetcode solution
    def findShortestSubArray2(self, nums: List[int]) -> int:
        freq = {}  # map num to indices
        for i, n in enumerate(nums):
            if n in freq:
                freq[n].append(i)
            else:
                freq[n] = [i]
        deg = max([len(i) for i in freq.values()])  # based on indices calc degree
        return min([i[-1] - i[0] for i in freq.values() if len(i) == deg]) + 1

    # Accepted but slow, 10%
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        deg = max(freq.values())
        freqNums = []
        for n, d in freq.items():
            if d == deg: freqNums.append(n)

        ans = len(nums)
        for n in freqNums:
            count, l, r, i = 0, 0, 0, 0
            while count < deg:
                if nums[i] == n:
                    if count == 0:
                        l, r = i, i
                    else:
                        r = i
                    count += 1
                i += 1
            length = r - l + 1
            ans = min(ans, length)
        return ans


obj = Solution()
# nums = [1, 2, 2, 3, 1]
nums = [1, 2, 2, 3, 1, 4, 2]
print(obj.findShortestSubArray(nums))
