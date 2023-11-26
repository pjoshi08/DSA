package org.example.blind;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        List<int []> output = new ArrayList<>();
        Arrays.sort(intervals, Comparator.comparingInt(i -> i[0]));
        int start = intervals[0][0];
        int end = intervals[0][1];

        int currStart, currEnd;
        for (int i=1; i < intervals.length; i++) {
            currStart = intervals[i][0];
            currEnd = intervals[i][1];
            if (currStart <= end) {
                end = Math.max(end, currEnd);
            } else {
                output.add(new int[]{start, end});
                start = currStart;
                end = currEnd;
            }
        }

        output.add(new int[]{start, end});
        return output.toArray(new int[output.size()][]);
    }
}
