# Minimum Number of Pushes to Type Word I:
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/
class Solution:
    def minimumPushes(self, word: str) -> int:
        quotient, remain, n, row = 0, 0, len(word), 1
        res = 0

        # 2-9 account for 8 keys
        quotient = n // 8  # to calculate the number of complete loops we'd have to make
        remain = n % 8  # to calculate the remaining number of characters to cover that fall short of a complete loop

        while quotient > 0:
            res += 8 * row

            quotient -= 1
            row += 1

        res += remain * row
        return res
