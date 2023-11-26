package org.example.tree;

public class MaxPathSum {

    int max = 0;
    public int maxPathSum(TreeNode root) {
        max = root.val;
        dfs(root);
        return max;
    }

    private int dfs(TreeNode root) {
        if (root == null) return 0;

        int leftMax = dfs(root.left);
        int rightMax = dfs(root.right);
        leftMax = Math.max(leftMax, 0);
        rightMax = Math.max(rightMax, 0);

        max = Math.max(max, root.val + leftMax + rightMax);

        return root.val + Math.max(leftMax, rightMax);
    }
}
