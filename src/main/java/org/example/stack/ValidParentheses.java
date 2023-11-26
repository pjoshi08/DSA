package org.example.stack;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<Character, Character>() {{
            put('}', '{');
            put(']', '[');
            put(')', '(');
        }};

        Stack<Character> stack = new Stack<>();

        for (char c: s.toCharArray()) {
            if (map.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == map.get(c)) {
                    stack.pop();
                } else
                    return false;
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}
