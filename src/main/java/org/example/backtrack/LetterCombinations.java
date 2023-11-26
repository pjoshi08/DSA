package org.example.backtrack;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// T = 5ms
public class LetterCombinations {

    List<String> res = new ArrayList<>();
    Map<Character, String> map = new HashMap<>();

    public List<String> letterCombinations(String digits) {

        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        if (!digits.isEmpty()) dfs(0, digits, "");
        return res;
    }

    private void dfs(int i, String digits, String s) {
        if (s.length() == digits.length()) {
            res.add(s);
            return;
        }

        for (char c : map.get(digits.charAt(i)).toCharArray()) {
            dfs(i + 1, digits, s + c);
        }
    }

    public static void main(String[] args) {
        String digits = "23";
        System.out.println(new LetterCombinations().letterCombinations(digits));
    }
}

// T = 1ms
class SolutionLetterCombinations {
    public List<String> letterCombinations(String digits) {

        if(digits.isEmpty()){
            return new ArrayList<>();
        }
        HashMap<Integer, String> phone = new HashMap<>();
        phone.put(2, "abc");
        phone.put(3, "def");
        phone.put(4, "ghi");
        phone.put(5, "jkl");
        phone.put(6, "mno");
        phone.put(7, "pqrs");
        phone.put(8, "tuv");
        phone.put(9, "wxyz");

        List<String> ans = new ArrayList<String>();
        backtrack(new StringBuilder(), ans, digits, phone);
        return ans;
    }

    private void backtrack(StringBuilder path, List<String> ans, String digits, Map<Integer, String> phone){
        if(digits.isEmpty()){
            ans.add(path.toString());
            return;
        }

        for(char c : phone.get(Character.getNumericValue(digits.charAt(0))).toCharArray()){
            path.append(c);
            backtrack(path, ans, digits.substring(1), phone);
            path.deleteCharAt(path.length() - 1);
        }


    }
}
