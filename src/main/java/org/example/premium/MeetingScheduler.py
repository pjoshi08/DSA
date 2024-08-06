import heapq
from typing import List

# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
# return the earliest time slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements, return an empty array.
#
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from
# start to end.
#
# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any
# two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

# Example 1:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]
# Example 2:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []
class Solution:
    # O(nlogn + mlogm)
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            # find left and right itersection
            right = min(slots1[p1][1], slots2[p2][1])  # choose the slot that ends earlier
            left = max(slots1[p1][0], slots2[p2][0])  # choose the slot that starts later for overlap
            if right - left >= duration:  # if cur overlap is valid
                return [left, left + duration]
            # shift the slot will ends earlier
            if slots1[p1][1] <= slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []

    # O((n + m)log(n + m))
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # create a list that only contains valid intervals for both slots
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)

        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]  # we don't pop the next slot straight away
            # s1 = [60, 70], s2 = [60, 120], d = 8 => 70 >= 60 + d, for valid overlap
            if end1 >= start2 + duration:  # if the first slot ends after the start of next slot + d
                return [start2, start2 + duration]  # start2 because it might start later
        return []