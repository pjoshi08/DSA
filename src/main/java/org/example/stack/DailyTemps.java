package org.example.stack;

import java.util.Stack;

public class DailyTemps {

    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        /*Stack<<Integer, Integer>> stack = new Stack<>();

        for (int i=0; i < temperatures.length; i++) {
            if (!stack.isEmpty() && stack.peek().fst < temperatures[i]) {
                int index = stack.pop().snd;
                res[index] = i - index;
            } else {
                stack.push(new Pair<>(temperatures[i], i));
            }
        }*/

        return res;
    }
}
