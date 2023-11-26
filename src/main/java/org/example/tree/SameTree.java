package org.example.tree;

public class SameTree {

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;

        if (p == null) return false;
        if (q == null) return false;
        boolean leftSub = p.val == q.val && isSameTree(p.left, q.left);
        boolean rightSub = p.val == q.val && isSameTree(p.right, q.right);

        return leftSub & rightSub;
    }


}
