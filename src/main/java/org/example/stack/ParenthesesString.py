# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0: return False

        def validate(s, locked, op):
            bal, wild = 0, 0
            for i, c in enumerate(s):
                if locked[i] == "1":
                    bal += 1 if c == op else -1
                else:
                    wild += 1
                if bal + wild < 0:
                    return False
            return bal <= wild

        return validate(s, locked, "(") and validate(s[::-1], locked[::-1], ")")


obj = Solution()
# s = "))()))"
# s = "()()"
# s = ")"
s = "()"
# locked = "010100"
# locked = "0000"
# locked = "0"
locked = "11"
print(obj.canBeValid(s, locked))
