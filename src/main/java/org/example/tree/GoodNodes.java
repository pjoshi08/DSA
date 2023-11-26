package org.example.tree;

public class GoodNodes {

    // Preorder traversal
    public int goodNodes(TreeNode root) {
        return dfs(root, root.val);
    }

    private int dfs(TreeNode node, int max) {
        if (node == null) return 0;

        int res = node.val >= max ? 1 : 0;
        max = Math.max(max, node.val);
        res += dfs(node.left, max);
        res += dfs(node.right, max);

        return res;
    }
}
