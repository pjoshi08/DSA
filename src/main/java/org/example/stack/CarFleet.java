package org.example.stack;

import java.util.*;

public class CarFleet {

    public int carFleet(int target, int[] position, int[] speed) {
        Stack<Float> stack = new Stack<>();
        Map<Integer, Integer> pairs = new TreeMap<>(Collections.reverseOrder());

        for (int i=0; i<position.length;i++) pairs.put(position[i], speed[i]);

        for (Map.Entry<Integer, Integer> entry : pairs.entrySet()) {
            int dist = target - entry.getKey();
            float time = (float) dist / entry.getValue();
            stack.push(time);
            if (stack.size() >= 2 && stack.peek() <= stack.elementAt(stack.size()-2)) {
                stack.pop();
            }
        }

        return stack.size();
    }
}
