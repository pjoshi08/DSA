package org.example.tree;

// Lowest Common Ancestor of a Binary Search Tree
public class LCABST {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p == root && q == root) return root;
        
        if (p.val < root.val && q.val < root.val)
            root = lowestCommonAncestor(root.left, p, q);
        if (p.val > root.val && q.val > root.val)
            root = lowestCommonAncestor(root.right, p, q);

        return root;
    }
}
