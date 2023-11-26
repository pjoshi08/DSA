package org.example.binarysearch;

public class MinRotatedArr {

    public int findMin(int[] nums) {

        for (int i=0; i<nums.length-1; i++) {
            if (nums[i+1] < nums[i]) return nums[i+1];
            if (i == nums.length-2) return nums[0];
        }

        return nums[0];
    }

    // Solution 2
    public int findMin2(int[] nums) {
        if (nums.length == 1) return nums[0];
        int left = 0, right = nums.length - 1;
        int res = 0;

        while (left <= right) {
            if (nums[left] < nums[right]) {
                res = Math.min(res, nums[left]);
                break;
            }

            int mid  = left + (right - left)/2;
            res = Math.min(res, nums[mid]);
            if (nums[mid] >= nums[left]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return res;
    }
}
