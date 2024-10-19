from typing import List


class Solution:
    def minimumBitwiseArray(self, nums: List[int]) -> List[int]:
        def find_x(num):
            for x in range(1, num):
                if x | (x + 1) == num:
                    return x
            return -1

        return [find_x(num) for num in nums]


# Example usage
nums = [2, 3, 5, 7]
solution = Solution()
result = solution.minimumBitwiseArray(nums)
print(result)  # Expected output: [-1, 1, 4, 3]
