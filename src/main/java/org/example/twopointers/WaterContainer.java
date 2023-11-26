package org.example.twopointers;

public class WaterContainer {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int l = 0, r = height.length-1;

        while (l < r) {
            int area = Math.min(height[l], height[r]) * (r - l);
            maxArea = Math.max(maxArea, area);

            if (height[l] < height[r]) l += 1;
            else if (height[l] > height[r]) r -= 1;
            else {
                if (height[l+1] < height[r-1]) l +=1;
                else if (height[l+1] > height[r-1]) r -= 1;
                else {
                    l += 1;
                }
            }
        }

        return maxArea;
    }
}
