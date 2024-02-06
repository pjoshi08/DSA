class Solution(object):
    def isValid(self, s):
        dict = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c in dict:
                if stack and stack[-1] == dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False 


obj = Solution()
# s = "()"
# s = "()[]{}"
# s = "(]"
s = "((([])))"
print(obj.isValid(s))