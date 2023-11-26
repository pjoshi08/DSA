package org.example.tree;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;

public class ConstructBTFromTraversals {

    Map<Integer, Integer> nodeIndexMap = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int len = preorder.length;
        if (len == 0) return null;

        int i=0;
        for (int val: inorder) { nodeIndexMap.put(val, i++); }

        return buildTree(preorder, inorder, 0, len-1, 0, len-1);
    }

    private TreeNode buildTree(int[] preorder, int[] inorder,
                      int preStart, int preEnd,
                      int inStart, int inEnd) {
        if (preStart > preEnd || inStart > inEnd) return null;

        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = nodeIndexMap.get(preorder[preStart]);
        int leftEnd = inIndex - inStart;

        root.left = buildTree(preorder, inorder,
                preStart+1, preStart+leftEnd,
                    inStart, inIndex-1);
        root.right = buildTree(preorder, inorder,
                preStart+leftEnd+1, preEnd+leftEnd,
                inIndex+1, inEnd);

        return root;
    }


    // Slow
    public TreeNode buildTree2(int[] preorder, int[] inorder) {
        if (preorder.length == 0 || inorder.length == 0) return null;

        TreeNode root = new TreeNode(preorder[0]);
        int mid=0;
        for(int i=0; i < inorder.length; i++) {
            if (preorder[0] == inorder[i]) mid = i;
        }

        root.left = buildTree2(
                Arrays.copyOfRange(preorder, 1, mid+1),
                Arrays.copyOfRange(inorder, 0, mid)
        );

        root.right = buildTree2(
                Arrays.copyOfRange(preorder, mid+1, preorder.length-1),
                Arrays.copyOfRange(inorder, mid+1, inorder.length-1)
        );

        return root;
    }

    public static void main(String[] args) {
        int[] preorder = {3,9,20,15,7};
        int[] inorder = {9,3,15,20,7};
        System.out.println(new ConstructBTFromTraversals().buildTree(preorder, inorder));
    }
}
