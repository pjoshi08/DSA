class Solution:
    # O(log n)
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i_x = 1  # to get the ith bit in x
        i_n = 1  # to get the ith bit for n - 1 values

        while i_n <= n - 1:  # to get n - 1 values
            if i_x & x == 0:  # if ith bit in x is 0
                if i_n & (n - 1):  # if ith bit for cur num is 1
                    res = res | i_x
                i_n = i_n << 1
            i_x = i_x << 1

        return res
