class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = 0
        while True:
            prod = 1
            num = n + i
            candidate = num
            while candidate:
                digit = candidate % 10
                prod *= digit
                candidate = candidate // 10
            if prod % t == 0: break
            i += 1

        return num


solution = Solution()
print(solution.smallestNumber(10, 2))
print(solution.smallestNumber(15, 3))
print(solution.smallestNumber(17, 6))
