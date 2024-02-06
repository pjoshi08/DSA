class Solution(object):
    def sumOfThree(self, num):
        num1 = num // 3
        num0 = num1 - 1
        num2 = num1 + 1
        if (num1 + num0 + num2) == num:
            return [num0, num1, num2]
        else:
            return []

obj = Solution()
# num = 33
num = 4
print(obj.sumOfThree(num))