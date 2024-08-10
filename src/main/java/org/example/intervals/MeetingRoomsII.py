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

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        s, e = 0, 0  # for start index and end index
        res = count = 0

        while s < len(intervals):
            if start[s] < end[e]:  # capture all the intervals that overlap in an interval
                # increase room count because they overlap
                count += 1
                s += 1
            else:  # reached a meeting interval that doesn't overlap
                count -= 1
                e += 1
            res = max(res, count)
        return res


obj = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(obj.minMeetingRooms(intervals))
