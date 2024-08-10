from typing import List


class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        n = len(intervals)
        i = 0
        while i < n:
            start, end = intervals[i]
            while i + 1 < n and end >= intervals[i + 1][0]:
                end = max(end, intervals[i + 1][1])
                i += 1
            res.append([start, end])
            i += 1
        return res
