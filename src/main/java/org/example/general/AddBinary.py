# Add Binary: https://leetcode.com/problems/add-binary/
# Similar to AddTwoNumbers in LL

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        res = ""
        carry, i = 0, 0
        l1, l2 = len(a), len(b)
        l3 = max(l1, l2)
        while i < l3 or carry:
            v1 = int(a[i]) if i < l1 else 0
            v2 = int(b[i]) if i < l2 else 0

            dig = (v1 + v2 + carry) % 2
            carry = (v1 + v2 + carry) // 2
            res += str(dig)
            i += 1
        return res[::-1]
