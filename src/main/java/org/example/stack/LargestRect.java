package org.example.stack;

import java.util.Stack;

public class LargestRect {

    /*public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<Pair<Integer, Integer>> stack = new Stack<>();

        for (int i=0; i < heights.length; i++) {
            int start = i;
            while (!stack.isEmpty() && stack.peek().getValue() > heights[i]) {
                Pair<Integer, Integer> pair = stack.pop();
                maxArea = Math.max(maxArea, pair.getValue() * (i - pair.getKey()));
                start = pair.getKey();
            }
            stack.push(new Pair<>(start, heights[i]));
        }

        for (Pair<Integer, Integer> pair: stack) {
            maxArea = Math.max(maxArea, pair.getValue() * (heights.length - pair.getKey()));
        }

        return maxArea;
    }*/
}
