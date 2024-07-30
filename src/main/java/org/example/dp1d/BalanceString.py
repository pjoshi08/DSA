class Solution:
    # T: O(n), M: O(1)
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        deletions = 0
        b = 0
        for c in s:  # the index value starts from 1 but string iterates from the beginning
            if c == "b":
                b += 1
            else:
                # calc deletions when you see a
                # set it to the min of increased deletions or the b count encountered till now
                deletions = min(deletions + 1, b)
        return deletions

    # T: O(n), M: O(n)
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        b = 0
        for i, c in enumerate(s, 1):  # the index value starts from 1 but string iterates from the beginning
            if c == "b":
                f[i] = f[i - 1]
                b += 1
            else:
                f[i] = min(f[i - 1] + 1, b)
        return f[n]

    # The intuition behind the solution is to find the point where all chars to the left are a and
    # all to the right are b to make the string is balanced
    # it doesn't matter what the char at the middle point is but only whats left to it and whats right
    # check example 1
    # T: O(n), M: O(1), slower than the 1st solution
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a_right = 0
        for c in s:  # count a
            count_a_right += 1 if c == "a" else 0

        count_b_left = 0
        res = n  # at max we can do n deletions
        for c in s:
            if c == "a": count_a_right -= 1  # as we traverse s, if c == a, count a should be dec
            res = min(res, count_a_right + count_b_left)
            if c == "b": count_b_left += 1
        return res

    # T: O(n), M: O(n), slowest solution
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a_right = [0] * n
        for i in range(n - 2, -1, -1):  # n - 2 because there's nothing to the right of last index
            count_a_right[i] = count_a_right[i + 1]
            count_a_right[i] += 1 if s[i + 1] == "a" else 0  # +1 if char next to i is a

        count_b_left = 0
        res = n  # at max we can do n deletions
        for i, c in enumerate(s):
            res = min(res, count_a_right[i] + count_b_left)
            if c == "b": count_b_left += 1
        return res