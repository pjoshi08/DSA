from typing import List


class Solution:
    # T: O(max(N, M)), M: O(1), one pass, two pointer solution
    def compareVersion(self, version1: str, version2: str) -> int:
        def getNum(s: str, i: int, n: int) -> List[int]:
            num = 0
            while i < n:
                if s[i] == ".":
                    break
                num = num * 10 + int(s[i])
                i += 1
            return [num, i + 1]  # increase index for the next getNum() call

        n1, n2 = len(version1), len(version2)
        i = j = 0
        while i < n1 or j < n2:
            num1, i = getNum(version1, i, n1)
            num2, j = getNum(version2, j, n2)
            if num1 != num2:
                return -1 if num1 < num2 else 1
        return 0

    # T: O(N+M+max(N,M)), M: O(n), slower solution
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                if i1 < i2: return -1
                else: return 1
        return 0