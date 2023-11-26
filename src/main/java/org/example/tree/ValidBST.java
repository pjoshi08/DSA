package org.example.tree;

public class ValidBST {

    public boolean isValidBST(TreeNode root) {
        return isValid(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
    }

    private boolean isValid(TreeNode node, double left, double right) {
        if (node == null) return true;
        if (!(node.val > left && node.val < right)) return false;

        return (isValid(node.left, left, node.val) && isValid(node.right, node.val, right));
    }
}
