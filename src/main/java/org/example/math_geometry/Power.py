class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x * x, n // 2)  # instead of x * x, we can also do res = res * res
            # before returning (but that is slower)
            return x * res if n % 2 else res  # handle odd power
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res  # handle negative power
