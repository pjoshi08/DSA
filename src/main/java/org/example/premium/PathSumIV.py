# If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers.
# For each integer in this array:
#
# The hundreds digit represents the depth d of this node where 1 <= d <= 4. The tens digit represents the position p
# of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
# The units digit represents the value v of this node where 0 <= v <= 9. Given an array of ascending three-digit
# integers nums representing a binary tree with a depth smaller than 5, return the sum of all paths from the root
# towards the leaves.
#
# It is guaranteed that the given array represents a valid connected binary tree.
#
# Input: nums = [113,215,221]
# Output: 12
# Explanation: The tree that the list represents is shown.
# The path sum is (3 + 5) + (3 + 1) = 12.
#
# Input: nums = [113,221]
# Output: 4
# Explanation: The tree that the list represents is shown.
# The path sum is (3 + 1) = 4.
class Solution:
    def pathSum(self, nums):
        if not nums:
            return 0

        # Store the data in a hashmap, with the coordinates as the key and the node value as the value
        coord_map = {}
        for element in nums:
            coordinates = element // 10
            value = element % 10
            coord_map[coordinates] = value

        # Pass the initial sum value in the sum function.
        return self.dfs(nums[0] // 10, 0, coord_map)

    def dfs(self, root_coordinates, pre_sum, coord_map):
        # Find the level and position values from the coordinates.
        level = root_coordinates // 10
        position = root_coordinates % 10

        # Find out the left child and right child positions of the tree.
        left = (level + 1) * 10 + position * 2 - 1
        right = (level + 1) * 10 + position * 2
        curr_sum = pre_sum + coord_map[root_coordinates]

        # If left child and right child do not exist, return.
        if not left in coord_map and not right in coord_map:
            return curr_sum

        # Otherwise iterate through the left and right children recursively using depth first search.
        left_sum = (
            self.dfs(left, curr_sum, coord_map) if left in coord_map else 0
        )
        right_sum = (
            self.dfs(right, curr_sum, coord_map) if right in coord_map else 0
        )
        return left_sum + right_sum
