from typing import List


# You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].
#
# You have an array arr of length length with all zeros, and you have some operation to apply on arr.
# In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ...,
# arr[endIdxi] by inci.
#
# Return arr after applying all the updates.
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length + 1)
        for start, end, inc in updates:
            arr[start] += inc
            arr[end + 1] -= inc
        for i in range(1, length + 1):
            arr[i] += arr[i - 1]

        return arr[:-1]
