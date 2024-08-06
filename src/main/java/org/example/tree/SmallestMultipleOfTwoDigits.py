from collections import deque


# Given three integers, k, digit1, and digit2, you want to find the smallest integer that is:
#
# Larger than k,
# A multiple of k, and
# Comprised of only the digits digit1 and/or digit2.
# Return the smallest such integer. If no such integer exists or the integer exceeds the limit of a
# signed 32-bit integer (231 - 1), return -1.
# Example 1:
#
# Input: k = 2, digit1 = 0, digit2 = 2
# Output: 20
# Explanation:
# 20 is the first integer larger than 2, a multiple of 2, and comprised of only the digits 0 and/or 2.
# Example 2:
#
# Input: k = 3, digit1 = 4, digit2 = 2
# Output: 24
# Explanation:
# 24 is the first integer larger than 3, a multiple of 3, and comprised of only the digits 4 and/or 2.
# Example 3:
#
# Input: k = 2, digit1 = 0, digit2 = 0
# Output: -1
# Explanation:
# No integer meets the requirements so return -1.
class Solution:
    # BFS solution
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        d1, d2 = min(digit1, digit2), max(digit1, digit2)
        q = deque()
        if d1 != 0: q.append(d1)
        if d2 != 0: q.append(d2)
        if d1 == d2 and q: q.popleft()
        limit = 2 ** 31
        while q:
            n = q.popleft()
            if n > k and n % k == 0: return n
            if n * 10 + d1 < limit: q.append(n * 10 + d1)
            if d1 != d2 and n * 10 + d2 < limit: q.append(n * 10 + d2)
        return -1
