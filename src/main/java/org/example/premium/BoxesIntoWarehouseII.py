# Boxes are put into the warehouse by the following rules:
#
# Boxes cannot be stacked.
# You can rearrange the insertion order of the boxes.
# Boxes can be pushed into the warehouse from either side (left or right)
# If the height of some room in the warehouse is less than the height of a box, then that box and
# all other boxes behind it will be stopped before that room.
# Return the maximum number of boxes you can put into the warehouse.
# https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/description/
from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()

        l, r = 0, len(warehouse) - 1
        count, box_idx = 0, len(boxes) - 1

        while l <= r and box_idx >= 0:  # consider largest box first
            # Check if the current box can fit in the
            # leftmost available room
            if boxes[box_idx] <= warehouse[l]:
                l += 1
                count += 1
            # Check if the current box can fit in the
            # rightmost available room
            elif boxes[box_idx] <= warehouse[r]:
                r -= 1
                count += 1
            box_idx -= 1
        return count

# boxes = [1, 2, 2, 3, 4]
# warehouse = [3, 4, 1, 2]
