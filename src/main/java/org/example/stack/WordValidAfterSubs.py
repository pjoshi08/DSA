# Check word is valid after substitutions
class Solution(object):

    def isValid(self, s):
        if len(s) < 3: return False
        stack = []

        for c in s:
            stack.append(c)
            if len(stack) >= 3:
                if stack[-1] == "c" and stack[-2] == "b" and stack[-3] == "a":
                    stack.pop()
                    stack.pop()
                    stack.pop()
        return not stack

    # Correct but a simpler solution exists
    def isValid2(self, s):
        if len(s) < 3: return False
        dict = {"b": "a", "c": "b"}
        stack = []

        for c in s:
            if c in dict:
                if stack and stack[-1] == dict[c]:  # c is "b" or "c"
                    if c == "b": stack.append(c)
                    else:  # c == "c"
                        if len(stack) < 2: stack.append(c)
                        elif stack[-1] == "b" and stack[-2] == "a":
                            stack.pop()
                            stack.pop()
                        else:
                            stack.append(c)
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return True if not stack else False

obj = Solution()
# s = "aabcbc"
# s = "abcabcababcc"
# s = "abccba"
s = "babcc"
print(obj.isValid(s))
