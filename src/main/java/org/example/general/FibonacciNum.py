class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return 0
        if n == 2: return 1

        num1 = 0
        num2 = 1
        for i in range(n):
            temp = num2
            num2 = num1 + num2
            num1 = temp
        return num1
