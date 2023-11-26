package org.example.graph;

import java.util.*;

public class CourseSchedule {

    Map<Integer, List<Integer>> preqMap = new HashMap<>();
    Set<Integer> visit = new HashSet<>();
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for (int i=0; i < numCourses; i++)
            preqMap.put(i, new ArrayList<>());
        for (int[] prerequisite : prerequisites) {
            preqMap.get(prerequisite[0]).add(prerequisite[1]);
        }

        for (int crs=0; crs < numCourses; crs++) {
            if (!dfs(crs)) return false;
        }

        return true;
     }

    private boolean dfs(int crs) {
        if (visit.contains(crs)) return false;
        if (preqMap.get(crs).isEmpty()) return true;

        visit.add(crs);
        for (int pre: preqMap.get(crs))
            if (!dfs(pre)) return false;
        visit.remove(crs);
        preqMap.put(crs, new ArrayList<>());
        return true;
    }
}
