package org.example.graph;

import java.util.HashMap;

public class CloneGraph {

    HashMap<Node, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null || node.neighbors.isEmpty()) return null;
        return dfs(node);
    }

    private Node dfs(Node node) {
        if (map.containsKey(node)) return map.get(node);

        Node copy = new Node(node.val);
        map.put(node, copy);

        for (Node adj: node.neighbors) {
            copy.neighbors.add(dfs(adj));
        }

        return copy;
    }
}
