from typing import List


class Solution:
    # faster, maths based
    def sortJumbled2(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i, n in enumerate(nums):
            mapped_n, base = 0, 1
            if n == 0:
                mapped_n = mapping[n]
            while n > 0:
                digit = n % 10
                n = n // 10
                mapped_n += base * mapping[digit]
                base *= 10
            pairs.append((mapped_n, i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]

    # string based
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []  # (mappedNum, index)
        for i, n in enumerate(nums):
            n = str(n)
            mapped_n = 0
            for c in n:
                mapped_n *= 10
                mapped_n += mapping[int(c)]
            pairs.append((mapped_n, i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]


obj = Solution()
mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(obj.sortJumbled(mapping, nums))
