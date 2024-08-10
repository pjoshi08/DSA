from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]):
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1.end > i2.start: return False
        return True

    class Solution:
        def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
            if len(intervals) == 0: return True
            intervals.sort(key=lambda x: x[0])
            prevEnd = intervals[0][1]

            for start, end in intervals[1:]:
                if start < prevEnd: return False
                prevEnd = end
            return True
