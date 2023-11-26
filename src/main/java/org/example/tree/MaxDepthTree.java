package org.example.tree;

public class MaxDepthTree {

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        return calcDepth(root, 1);
    }

    private int calcDepth(TreeNode node, int depth) {
        if (node == null || (node.left == null && node.right == null)) return depth;

        int leftDepth = 0, rightDepth = 0;
        if (node.left != null) {
            leftDepth = Math.max(depth, calcDepth(node.left, depth + 1));
        }
        if (node.right != null) {
            rightDepth = Math.max(depth, calcDepth(node.right, depth + 1));
        }

        return Math.max(leftDepth, rightDepth);
    }

    public static void main(String[] args) {
        TreeNode node7 = new TreeNode(7, null, null);
        TreeNode node15 = new TreeNode(15, null, null);
        TreeNode node20 = new TreeNode(20, node15, node7);
        TreeNode node9 =  new TreeNode(9, null, null);
        TreeNode node3 = new TreeNode(3, node9, node20);

        System.out.println(new MaxDepthTree().maxDepth(node3));
    }
}
