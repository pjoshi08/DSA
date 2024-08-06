
# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/solutions/3006557/maximise-minimise-patterns-very-descriptive-greedy-math/?envType=company&envId=paypal&favoriteSlug=paypal-all&difficulty=MEDIUM
class Solution:
    # Intuition is that to get the smallest product between x and y, x and y should be as far apart
    # as possible
    def minNonZeroProduct(self, p: int) -> int:
        """
        0001
        0010

        1110: each one is 2^p - 2 and there are ((2^p / 2) - 1) pairs
        1111: 2^p - 1
        """
        mod = 10 ** 9 + 7
        top = pow(2, p, mod) - 1
        second_largest = top - 1
        count = pow(2, p - 1) - 1

        return (pow(second_largest, count, mod) * top) % mod