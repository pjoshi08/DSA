package org.example.tree;

public class TreeDiameter {

    private int maxD = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) return 0;

        dfs(root);

        return maxD;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;

        int left = dfs(node.left);
        int right = dfs(node.right);

        // Diameter = (maxL + 1) + (maxR + 1)
        maxD = Math.max(maxD, left + right);

        // this calculates height
        return 1 + Math.max(left, right);
    }
}
