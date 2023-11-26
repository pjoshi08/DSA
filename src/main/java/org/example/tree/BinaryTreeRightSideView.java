package org.example.tree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinaryTreeRightSideView {

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            TreeNode rightSide = null;
            int qLen = q.size();

            for (int i=0; i<qLen; i++) {
                TreeNode node = q.remove();
                if (node != null) {
                    rightSide = node;
                    q.add(node.left);
                    q.add(node.right);
                }
            }
            if (rightSide != null) {
                res.add(rightSide.val);
            }
        }

        return res;
    }

    // BFS
    public List<Integer> rightSideView2(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int qLen = q.size();
            List<Integer> level = new ArrayList<>();

            for (int i=0; i<qLen; i++) {
                TreeNode node = q.remove();
                if (node != null) {
                    level.add(node.val);
                    q.add(node.left);
                    q.add(node.right);
                }
            }
            if (!level.isEmpty()) res.add(level.get(level.size()-1));
        }

        return res;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        TreeNode n3 = new TreeNode(3);
        TreeNode n4 = new TreeNode(4);
        root.left = n2; root.right = n3;
        n2.left = n4;

        System.out.println(new BinaryTreeRightSideView().rightSideView(root));
    }
}
