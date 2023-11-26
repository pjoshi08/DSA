package org.example.heap_pq;

import java.util.Collections;
import java.util.PriorityQueue;

public class KthLargest {

    // Quick select, T = O(n) average case; O(n^2) worst case
    public int findKthLargest(int[] nums, int k) {
        k = nums.length - k;
        return quickSelect(0, nums.length-1, k, nums);
    }

    private int quickSelect(int l, int r, int k, int[] nums) {
        int pivot = nums[r], p = l;
        int temp=0;
        for (int i=l; i < r; i++) {
            if (nums[i] <= pivot) {
                temp = nums[p];
                nums[p] = nums[i];
                nums[i] = temp;
                p += 1;
            }
        }
        temp = nums[p];
        nums[p] = nums[r];
        nums[r] = temp;

        if (p > k) return quickSelect(l, p - 1, k, nums);
        if (p < k) return quickSelect(p+1, r, k, nums);
        else return nums[p];
    }

    // T = O(n + k * logn); in worst case it is greater than nlogn
    public int findKthLargest2(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int n: nums) maxHeap.add(n);

        while (k > 1) {
            maxHeap.poll(); k -= 1;
        }
        return maxHeap.peek();
    }

    public static void main(String[] args) {
        int[] nums = {3,2,1,5,6,4};
        System.out.println(new KthLargest().findKthLargest(nums, 2));
    }
}
