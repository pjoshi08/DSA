from typing import List


class Solution:
    # T: O(n^2), M: O(1)
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        n = len(rating)
        for m in range(1, n - 1):
            # calculate ascending teams
            left_smaller = right_larger = 0
            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller += 1
            for i in range(m + 1, n):
                if rating[i] > rating[m]:
                    right_larger += 1
            res += left_smaller * right_larger

            # calculate descending teams
            left_larger = m - left_smaller
            right_smaller = (n - 1) - m - right_larger
            res += left_larger * right_smaller
        return res

    # caching solution, T: O(n^2), M: O(n), 5%, slowest
    def numTeams2(self, rating: List[int]) -> int:
        cache = {}
        length = len(rating)
        def backtrack(i, ascend, count):
            nonlocal length
            if (i, ascend, count) in cache:
                return cache[(i, ascend, count)]
            if count == 3: return 1
            if i == length: return 0

            res = 0
            for j in range(i + 1, length):
                if ascend and rating[i] < rating[j]:
                    res += backtrack(j, ascend, count + 1)
                if not ascend and rating[i] > rating[j]:
                    res += backtrack(j, ascend, count + 1)
            cache[(i, ascend, count)] = res
            return res

        res = 0
        for i in range(length):
            res += backtrack(i, True, 1)
            res += backtrack(i, False, 1)
        return res

    # dp solution, T: O(n^2), M: O(n), 7%
    def numTeams3(self, rating: List[int]) -> int:
        length = len(rating)
        ascend = [[0] * 4 for _ in range(length)]
        descend = [[0] * 4 for _ in range(length)]

        for i in range(length):  # for group len 1, we mark them as 1
            ascend[i][1] = 1
            descend[i][1] = 1

        for count in range(2, 4):  # calculate for group len 2 and 3
            for i in range(length):
                for j in range(i + 1, length):
                    if rating[i] < rating[j]:  # ascend condition
                        ascend[i][count] += ascend[j][count - 1]
                    if rating[i] > rating[j]:  # descend
                        descend[i][count] += descend[j][count - 1]

        res = 0
        for i in range(length):
            res += ascend[i][3] + descend[i][3]
        return res
