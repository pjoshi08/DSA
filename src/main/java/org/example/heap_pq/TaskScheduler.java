package org.example.heap_pq;

import org.example.Pair;

import java.util.*;

public class TaskScheduler {

    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c: tasks) map.put(c, map.getOrDefault(c, 0) + 1 );
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(map.values());

        int time=0, cnt;
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();
        while (!maxHeap.isEmpty() || !q.isEmpty()) {
            time += 1;
            if (!maxHeap.isEmpty()) {
                cnt = maxHeap.poll() - 1;
                if (cnt != 0) q.add(new Pair<>(cnt, time + n));
            }
            if (!q.isEmpty() && q.peek().getValue() == time)
                maxHeap.add(q.remove().getKey());
        }

        return time;
    }

    public static void main(String[] args) {
        char[] tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
        System.out.println(new TaskScheduler().leastInterval(tasks, 2));
    }
}
