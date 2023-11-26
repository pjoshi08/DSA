package org.example.blind;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Stack;

public class TreeDepth {
    // Recursive DFS, O(n) time, M O(n) worst case(uneven tree)
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    public int maxDepthIterativeDFS(TreeNode root) {
        int res = 0;
        Stack<TreeNode> treeStack = new Stack<>();
        treeStack.push(root);
        Stack<Integer> depthStack =  new Stack<>();
        depthStack.push(1);

        while (!treeStack.empty()) {
            TreeNode node = treeStack.pop();
            int depth = depthStack.pop();

            if (node != null) {
                res = Math.max(res, depth);
                treeStack.push(node.left);
                depthStack.push(depth + 1);

                treeStack.push(node.right);
                depthStack.push(depth + 1);
            }
        }

        return res;
    }

    public int maxDepthBFS(TreeNode root) {
        if (root == null) return 0;

        int level = 0;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);

        while (!q.isEmpty()) {
            for (int i=0; i < q.size(); i++) {
                TreeNode node = q.poll();
                if (node.left != null) {
                    q.add(node.left);
                }
                if (node.right != null) {
                    q.add(node.right);
                }

                level += 1;
            }
        }

        return level;
    }
}


  //Definition for a binary tree node.
  class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
