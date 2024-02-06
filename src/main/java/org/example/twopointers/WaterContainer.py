class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            if area > maxArea: maxArea = area
        return maxArea


obj = Solution()
# height = [1,8,6,2,5,4,8,3,7]
height = [1, 1]
print(obj.maxArea(height))