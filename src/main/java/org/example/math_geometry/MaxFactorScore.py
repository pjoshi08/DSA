import math
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:

        def calculate_factor(arr):
            if len(arr) == 0: return 0
            if len(arr) == 1: return arr[0] * arr[0]
            return lcm_of_array(arr) * gcd_of_array(arr)

        def lcm_of_array(arr):
            lcm = arr[0]
            for i in range(1, len(arr)):
                num1 = lcm
                num2 = arr[i]
                gcd = 1
                # Finding GCD using Euclidean algorithm
                while num2 != 0:
                    temp = num2
                    num2 = num1 % num2
                    num1 = temp
                gcd = num1
                lcm = (lcm * arr[i]) // gcd
            return lcm

        def gcd_of_array(arr):
            gcd = arr[0]
            for i in range(1, len(arr)):
                gcd = math.gcd(gcd, arr[i])
            return gcd

        whole = calculate_factor(nums)  # without removing any element
        factor_scores = []
        for i in range(len(nums)):
            if i < len(nums) - 1:
                arr = nums[:i] + nums[i + 1:]
            else:
                arr = nums[:i]
            factor_scores.append(calculate_factor(arr))

        return max(whole, max(factor_scores))


obj = Solution()
print(obj.maxScore([2, 4, 8, 16]))
print(obj.maxScore([1, 2, 3, 4, 5]))
print(obj.maxScore([3]))
