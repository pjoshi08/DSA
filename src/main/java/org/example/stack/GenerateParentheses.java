package org.example.stack;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        Stack<String> stack = new Stack<>();
        List<String> res = new ArrayList<>();

        int openN=0, closedN=0;
        backPropagate(openN, closedN, res, stack, n);
        return res;
    }

    private void backPropagate(int openN, int closedN, List<String> res, Stack<String> stack, int n) {
        if (openN == n && closedN == n) {
            buildResult(res, stack, n * 2);
        }

        if (openN < n) {
            stack.push("(");
            backPropagate(openN + 1, closedN, res, stack, n);
            stack.pop();
        }

        if (closedN < openN) {
            stack.push(")");
            backPropagate(openN, closedN + 1, res, stack, n);
            stack.pop();
        }
    }

    private void buildResult(List<String> res, Stack<String> stack, int length) {
        StringBuilder builder = new StringBuilder();
        stack.forEach(s -> {
            if (builder.length() <= length) builder.append(s);

            if (builder.length() == length) {
                res.add(builder.toString());
                builder.setLength(0);
            }
        });
    }
}
