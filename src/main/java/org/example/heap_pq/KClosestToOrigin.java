package org.example.heap_pq;

import org.example.Pair;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class KClosestToOrigin {

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> minheap = new PriorityQueue<>(
                (p1, p2) -> distance(p2) - distance(p1));
        for (int[] point: points) {
            minheap.add(point);
            if (minheap.size() > k) minheap.poll();
        }
        int[][] res = new int[k][];
        for (int i=0; i < k; i++) res[i] = minheap.poll();
        return res;
    }

    private int distance(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }

    // T = O(nlogn), 34ms
    public int[][] kClosest2(int[][] points, int k) {
        PriorityQueue<Pair<Double, Integer>> pq = new PriorityQueue<>((o1, o2) -> {
            if(o1.getKey() < o2.getKey())
                return -1;
            else if (o1.getKey() > o2.getKey())
                return 1;
            return 0;
        });

        for (int i=0; i < points.length; i++) {
            double dist = Math.pow(points[i][0], 2) + Math.pow(points[i][1], 2);
            pq.add(new Pair<>(dist, i));
        }

        int[][] res = new int[k][2];
        int i=0;
        while (k > 0) {
            Pair<Double, Integer> pair = pq.remove();
            int index = pair.getValue();
            res[i][0] = points[index][0];
            res[i][1] = points[index][1];
            k -= 1;
            i += 1;
        }

        return res;
    }

    public static void main(String[] args) {
        int[][] points = {{1,3}, {-2,2}};
        //int[][] points = {{3,3}, {5,-1}, {-2,4}};
        System.out.println(Arrays.deepToString(new KClosestToOrigin().kClosest(points, 1)));
    }
}
