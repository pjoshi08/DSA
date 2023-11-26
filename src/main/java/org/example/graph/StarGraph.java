package org.example.graph;

// Undirected
public class StarGraph {

    public static int findCenter(int[][] edges) {
        int centerNode = 0;
        int size = edges.length;
        int centerNodeCount;

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < 2; j++) {
                centerNode = edges[i][j];
                centerNodeCount = 1;

                for (int k = i+1; k < size; k++) {
                    if (containsNode(edges[k], centerNode)) {
                        centerNodeCount++;
                    }
                }

                if (centerNodeCount == size) {
                    return centerNode;
                }
            }
        }

        return centerNode;
    }

    static boolean containsNode(int[] edge, int node) {
        return node == edge[0] || node == edge[1];
    }
}
