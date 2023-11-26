package org.example.graph;

import java.util.*;

public class CourseScheduleII {

    Map<Integer, List<Integer>> prereq = new HashMap<>();
    Set<Integer> visit = new HashSet<>();
    Set<Integer> cycle = new HashSet<>();
    List<Integer> res = new ArrayList<>();
    public int[] findOrder(int numCourses, int[][] prerequisites) {
         for (int i=0; i < numCourses; i++)
             prereq.put(i, new ArrayList<>());
         for (int[] pre: prerequisites)
             prereq.get(pre[0]).add(pre[1]);

         for (int crs=0; crs < numCourses; crs++) {
             if (!dfs(crs)) return new int[0];
         }

         return res.stream().mapToInt(i -> i).toArray();
    }

    private boolean dfs(int crs) {
        if (cycle.contains(crs)) return false;
        if (visit.contains(crs)) return true;

        cycle.add(crs);
        for (int pre: prereq.get(crs))
            if (!dfs(pre)) return false;
        cycle.remove(crs);
        visit.add(crs);
        res.add(crs);
        return true;
    }
}
