package org.example.tree;

public class BalancedBinaryTree {

    /*public boolean isBalanced(TreeNode root) {
        return dfs(root).getKey();
    }

    private Pair<Boolean, Integer> dfs(TreeNode node) {
        if (node == null) return new Pair<Boolean, Integer>(true, 0);

        Pair<Boolean, Integer> left = dfs(node.left);
        Pair<Boolean, Integer> right = dfs(node.right);

        boolean balanced = (left.getKey() && right.getKey() &&
                Math.abs(left.getValue() - right.getValue()) <= 1);

        return new Pair<Boolean, Integer>(balanced, 1 + Math.max(left.getValue(), right.getValue()));
    }*/

}
