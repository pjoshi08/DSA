package org.example.binarysearch;

import java.util.Arrays;

public class RotatedArrSearch {
    public int search(int[] nums, int target) {
        if (nums.length == 1) {
            if (nums[0] == target) return 0; else return -1;
        }

        int left = 0, right = nums.length-1;

        while (left <= right) {
            int mid = left + (right - left)/2;
            if (nums[mid] == target) return mid;

            // Check to see if target is in left sorted array
            if (nums[left] <= nums[mid]) {
                if (target > nums[mid] || target < nums[left]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
               // we are in right sorted portion
                if (target < nums[mid] || target > nums[right]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }

        return -1;
    }
}
