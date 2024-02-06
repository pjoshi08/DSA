class Solution(object):
    def twoSum(self, numbers, target):
        idx1, idx2 = 0, len(numbers) - 1

        for i in range(len(numbers)):
            if numbers[idx1] + numbers[idx2] == target:
                return [idx1 + 1, idx2 + 1]
            elif numbers[idx1] + numbers[idx2] < target:
                idx1 += 1
            elif numbers[idx1] + numbers[idx2] > target:
                idx2 -= 1
        return [idx1 + 1, idx2 + 1]
