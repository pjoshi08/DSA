from typing import List

from org.example.intervals.MeetingRooms import Interval


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s, e = 0, 0  # start index, end index
        res, count = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
