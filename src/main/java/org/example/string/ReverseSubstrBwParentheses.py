class Solution:
    # T: O(n), M: O(n)
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        parentheses_indices = []
        pairs = [0] * n

        # first pass to capture the parentheses pairs using stack
        # and store indices to teleport
        for i, c in enumerate(s):
            if c == "(":
                parentheses_indices.append(i)
            elif c == ")":
                j = parentheses_indices.pop()
                pairs[i] = j
                pairs[j] = i

        res = []
        idx = 0
        direction = 1

        while idx < n:
            if s[idx] == ")" or s[idx] == "(":
                # jump to index of the paired parentheses and reverse cur direction
                idx = pairs[idx]
                direction = -direction
            else:
                res.append(s[idx])
            idx += direction
        return "".join(res)

    # T: O(n^2), M: O(n), faster than the above
    def reverseParentheses2(self, s: str) -> str:
        res = []
        parentheses_indices = []

        for c in s:
            if c == "(":
                parentheses_indices.append(len(res))
            elif c == ")":
                start = parentheses_indices.pop()
                res[start:] = res[start:][::-1]  # reverse str
            else:
                res.append(c)
        return "".join(res)

    # T: O(n^2), M: O(n)
    def reverseParentheses3(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                rev = ""
                while stack and stack[-1] != "(":
                    rev += stack.pop()
                if stack: stack.pop()  # remove opening parentheses
                for c in rev:  # add reversed string back to stack
                    stack.append(c)
            else:
                stack.append(c)
        return "".join(stack)
