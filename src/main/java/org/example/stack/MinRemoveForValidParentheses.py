class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = right = 0
        stack = []
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                right += 1
                if right > left:
                    right -= 1
                    continue
            stack.append(c)

        # right parentheses will be balanced after 1 pass
        # now balance the left parantheses
        reverse = []
        for i in range(len(stack) - 1, -1, -1):
            c = stack[i]
            if c == "(":
                if left > right:
                    left -= 1
                    continue
            reverse.append(c)

        return "".join(reverse[::-1])