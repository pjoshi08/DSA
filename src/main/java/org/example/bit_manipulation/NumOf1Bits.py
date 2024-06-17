class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res

    # O(32) or O(1) but is inefficient for cases like 1000000001
    # but the runtime is quite similar as above
    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
