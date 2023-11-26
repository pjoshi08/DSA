package org.example.linkedlist;

public class DuplicateNumber {
    public int findDuplicate(int[] nums) {
        int slow = 0, fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        int slow2 = 0;
        do {
            slow = nums[slow];
            slow2 = nums[slow2];
        } while (slow != slow2);

        return slow;
    }

    public static void main(String[] args) {
        //int[] nums = {1,3,4,2,2};
        int[] nums = {3,1,3,4,2};
        System.out.println(new DuplicateNumber().findDuplicate(nums));
    }
}
