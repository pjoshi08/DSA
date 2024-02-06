from typing import List


class Solution:

    # O(n + m)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {n: -1 for n in nums1}

        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack[-1]] = n
                stack.pop()
            stack.append(n)

        for n in nums1:
            res.append(mapping[n])
        return res

    # O(n^2)
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            index = len(nums2) - 1
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]: index = j
                if j > index and nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res


obj = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
# nums1 = [2,4]
# nums2 = [1,2,3,4]
print(obj.nextGreaterElement(nums1, nums2))
