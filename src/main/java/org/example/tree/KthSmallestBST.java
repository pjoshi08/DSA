package org.example.tree;

import java.util.*;

public class KthSmallestBST {

    // T = O(n)
    public int kthSmallest(TreeNode root, int k) {
        if (root == null) return 0;
        int n=0;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;

        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.add(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            n += 1;
            if (n == k) return cur.val;

            cur = cur.right;
        }

        return root.val;
    }

    // Inefficient: T = O(n logn)
    public int kthSmallest2(TreeNode root, int k) {
        List<Integer> list = dfs(root, new ArrayList<>());
        Collections.sort(list);

        return list.get(k-1);
    }

    private List<Integer> dfs(TreeNode node, List<Integer> list) {
        if (node == null) return list;

        list.add(node.val);
        list = dfs(node.left, list);
        list = dfs(node.right, list);

        return list;
    }
}
