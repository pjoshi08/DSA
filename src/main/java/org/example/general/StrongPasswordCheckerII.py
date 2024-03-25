# Strong Password Checker II:
# https://leetcode.com/problems/strong-password-checker-ii/description/
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False

        lower, upper, digit, special = False, False, False, False
        specialChars = '!@#$%^&*()-+'

        for i in range(len(password)):
            if i + 1 < len(password) and password[i] == password[i + 1]:
                return False
            if not lower:
                lower = password[i].islower()
            if not upper:
                upper = password[i].isupper()
            if not digit:
                digit = password[i].isdigit()
            if not special:
                special = password[i] in specialChars

        return lower and upper and digit and special


obj = Solution()
password = "IloveLe3tcode!"
print(obj.strongPasswordCheckerII(password))
