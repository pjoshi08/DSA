class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1, num2, num3 = str(num1), str(num2), str(num3)
        while len(num1) < 4:
            num1 = "0" + num1
        while len(num2) < 4:
            num2 = "0" + num2
        while len(num3) < 4:
            num3 = "0" + num3

        key = []
        for i in range(4):
            key.append(str(min(int(num1[i]), int(num2[i]), int(num3[i]))))

        return int("".join(key))