from typing import List

# https://leetcode.com/problems/grumpy-bookstore-owner/description/
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        # calculating already satisfied customers
        for i in range(len(grumpy)):
            if not grumpy[i]:
                satisfied += customers[i]
                customers[i] = 0  # setting it to zero to not consider them again

        # rolling sum to calculate the best window to apply the minutes
        best_satisfied, current_satisfied = 0, 0
        for i in range(len(grumpy)):
            current_satisfied += customers[i]
            if i >= minutes:
                current_satisfied -= customers[i - minutes]  # removing customers from window
            best_satisfied = max(best_satisfied, current_satisfied)

        return satisfied + best_satisfied
