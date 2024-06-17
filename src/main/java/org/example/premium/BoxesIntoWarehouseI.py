# Boxes are put into the warehouse by the following rules:
#
# Boxes cannot be stacked.
# You can rearrange the insertion order of the boxes.
# Boxes can only be pushed into the warehouse from left to right only.
# If the height of some room in the warehouse is less than the height of a box, then that
# box and all other boxes behind it will be stopped before that room.
# Return the maximum number of boxes you can put into the warehouse.
# https://leetcode.com/problems/put-boxes-into-the-warehouse-i/
from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # pre-process warehouse heights to get usable heights
        # boxes can be pushed from left to right
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i - 1], warehouse[i])

        # sort boxes to greedily fit the boxes
        boxes.sort()
        count = 0

        # loop warehouse room in reverse, insert order l to r
        for room in reversed(warehouse):
            if count < len(boxes) and boxes[count] <= room:
                count += 1
        return count

# boxes = [4, 3, 4, 1]
# warehouse = [5, 3, 3, 4, 1]
