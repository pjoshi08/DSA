package org.example.tree;

public class SubTree {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // Null tree is a subTree of root(regardless of root is null or not)
        if (subRoot == null) return true;
        // Now since we already checked if subRoot is null, we only check if root is null or not
        if (root == null) return false;

        if (sameTree(root, subRoot)) return true;

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean sameTree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;

        if (root != null && subRoot != null && root.val == subRoot.val) {
            return sameTree(root.left, subRoot.left) && sameTree(root.right, subRoot.right);
        }

        return false;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(1);
        root.right = node2;
        TreeNode node3 = new TreeNode(1);
        node2.right = node3;
        TreeNode node4 = new TreeNode(1);
        node3.right = node4;
        TreeNode node5 = new TreeNode(1);
        node4.right = node5;
        TreeNode node6 = new TreeNode(1);
        node5.right = node6;
        TreeNode node7 = new TreeNode(1);
        node6.right = node7;
        TreeNode node8 = new TreeNode(1);
        node7.right = node8;
        TreeNode node9 = new TreeNode(1);
        node8.right = node9;
        TreeNode node10 = new TreeNode(1);
        node9.right = node10;
        TreeNode node11 = new TreeNode(1);
        node10.right = node11;
        node11.left = new TreeNode(2);

        TreeNode subRoot = new TreeNode(1);
        TreeNode subRoot2 = new TreeNode(1);
        subRoot.right = subRoot2;
        TreeNode subRoot3 = new TreeNode(1);
        subRoot2.right = subRoot3;
        TreeNode subRoot4 = new TreeNode(1);
        subRoot3.right = subRoot4;
        TreeNode subRoot5 = new TreeNode(1);
        subRoot4.right = subRoot5;
        TreeNode subRoot6 = new TreeNode(1);
        subRoot5.right = subRoot6;
        subRoot6.left = new TreeNode(2);

        System.out.println(new SubTree().isSubtree(root, subRoot));
    }
}
