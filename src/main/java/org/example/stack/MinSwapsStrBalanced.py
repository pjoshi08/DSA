# 1963. Minimum Number of Swaps to Make the String Balanced
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unbalanced = 0
        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if stack:  # if we are able to make a pair
                    stack.pop()
                else:
                    unbalanced += 1
        # unbalanced // 2 if unbalanced % 2 == 0 else unbalanced // 2 + 1
        return (unbalanced + 1) // 2

    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for c in s:
            if c == "[":
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2
