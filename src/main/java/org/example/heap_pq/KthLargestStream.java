package org.example.heap_pq;

import java.util.PriorityQueue;

public class KthLargestStream {

    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    int k;
    public KthLargestStream(int k, int[] nums) {
        this.k = k;
        for (int n: nums) minHeap.add(n);
        while (minHeap.size() > k) minHeap.remove();
    }

    public int add(int val) {
        minHeap.add(val);
        if (minHeap.size() > k) minHeap.remove();
        return minHeap.peek();
    }

    public static void main(String[] args) {
        int[] nums = {4,5,8,2};
        KthLargestStream kthLargest = new KthLargestStream(3, nums);
        System.out.println(kthLargest.add(3));
        System.out.println(kthLargest.add(5));
        System.out.println(kthLargest.add(10));
        System.out.println(kthLargest.add(9));
        System.out.println(kthLargest.add(4));
    }
}
