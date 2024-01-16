class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:  # same as one == 1
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]
