package org.example.dp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PascalTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(Arrays.asList(1)); if (numRows == 1) return ans;
        ans.add(Arrays.asList(1, 1)); if (numRows == 2) return ans;
        int leftIndex = 0, rightIndex = 1;
        for (int i = 3; i <= numRows; i++) { // loop for each row of the triangle
            List<Integer> prevList = ans.get(i-2);
            List<Integer> currList = new ArrayList<>();
            for (int j = 0; j <= i-1; j++) { // loop for populating the current row
                if (j == 0) {
                    currList.add(prevList.get(0));
                    continue;
                }
                if (j == i-1){
                    currList.add(prevList.get(prevList.size() - 1));
                    leftIndex = 0;
                    rightIndex = 1;
                    ans.add(currList);
                    continue;
                }

                int currentElement = prevList.get(leftIndex) + prevList.get(rightIndex);
                currList.add(currentElement);
                leftIndex++; rightIndex++;
            }
        }

        return ans;
    }
}
