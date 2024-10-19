# 921. Minimum Add to Make Parentheses Valid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened, closed = 0, 0
        for c in s:
            if c == "(":
                opened += 1
            else:
                opened -= 1
                if opened < 0:
                    opened = 0
                    closed += 1
        return opened + closed
