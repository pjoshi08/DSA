package org.example.binarysearch;

public class Search2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int[] row : matrix) {
            if (target <= row[row.length - 1])
                return binarySearch(row, target);
        }

        return false;
    }

    private boolean binarySearch(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target < nums[mid]) {
                right = mid - 1;
            } else if (target > nums[mid]) {
                left = mid + 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
