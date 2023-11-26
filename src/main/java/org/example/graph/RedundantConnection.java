package org.example.graph;

import java.util.*;

// Union Find Algorithm, T = O(n)
public class RedundantConnection {
    int[] par;
    int[] rank;
    public int[] findRedundantConnection(int[][] edges) {
        par = new int[edges.length + 1];
        rank = new int[edges.length + 1];
        int[] res = new int[2];
        for (int n=1; n <= edges.length; n++) {
            par[n] = n;
            rank[n] = 1;
        }

        for (int[] edge: edges) {
            if (!union(edge[0], edge[1])) {
                res[0] = edge[0];
                res[1] = edge[1];
                break;
            }
        }

        return res;
    }

    private int find(int n) {
        int p = par[n];
        while (p != par[p]) {
            par[p] = par[par[p]];
            p = par[p];
        }
        return p;
    }

    private boolean union(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);

        if (p1 == p2) return false;

        if (rank[p1] > rank[p2]) {
            par[p2] = p1;
            rank[p1] += rank[p2];
        } else {
            par[p1] = p2;
            rank[p2] += rank[p1];
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] edges = {{1,2}, {2,3}, {3,4}, {1,4}, {1,5}};
        System.out.println(Arrays.toString(new RedundantConnection().findRedundantConnection(edges)));
    }
}
