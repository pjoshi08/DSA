from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] or self.check(nums[i], nums[j]):
                    count += 1
        return count

    def check(self, num1, num2) -> bool:
        num1 = str(num1)
        num2 = str(num2)

        # add leading 0 for shorter num
        while len(num1) < len(num2):
            num1 = "0" + num1
        while len(num1) > len(num2):
            num2 = "0" + num2

        diff_count = 0
        first_idx, second_idx = -1, -1

        # capture indices where the two nums differ
        for i in range(len(num1)):
            if num1[i] != num2[i]:
                diff_count += 1
                if diff_count == 1:
                    first_idx = i
                elif diff_count == 2:
                    second_idx = i
                else:  # this condition means diff_count > 2, i.e. nums cannot be made equal
                    return False

        # if diff_count == 2, see if swapping values at indices makes two nums equal
        if diff_count == 2:
            num1 = list(num1)
            num1[first_idx], num1[second_idx] = num1[second_idx], num1[first_idx]
            num1 = ''.join(num1)
        return num1 == num2
