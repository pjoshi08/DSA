class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False

        while n % 5 == 0: n /= 5
        while n % 3 == 0: n /= 3
        while n % 2 == 0: n /= 2
        return n == 1


obj = Solution()
n = 14
#n = 6
#n = 1
#n = 256
print(obj.isUgly(n))
