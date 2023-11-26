package org.example.heap_pq;

import java.util.Collections;
import java.util.PriorityQueue;

public class LastStone {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int n: stones) pq.add(n);

        while (pq.size() != 1 && !pq.isEmpty()) {
            int y = pq.remove();
            int x = pq.remove();
            if (y - x > 0) pq.add(y - x);
        }
        if (pq.isEmpty()) return 0;
        return pq.peek();
    }

    public static void main(String[] args) {
        int[] stones = {2,7,4,1,8,1};
        System.out.println(new LastStone().lastStoneWeight(stones));
    }
}
