package org.example.heap_pq;

import org.example.Pair;

import java.util.*;

class Twitter {

    PriorityQueue<Pair<Pair<Integer, Integer>, Pair<Integer, Integer>>> maxHeap;
    int count;
    Map<Integer, List<Pair<Integer, Integer>>> tweetMap;
    Map<Integer, Set<Integer>> followMap;
    public Twitter() {
        count = 0;
        tweetMap = new HashMap<>();
        followMap = new HashMap<>();
    }

    public void postTweet(int userId, int tweetId) {
        List<Pair<Integer, Integer>> pairList = tweetMap.getOrDefault(userId, new ArrayList<>());
        pairList.add(new Pair<>(userId, tweetId));
        tweetMap.put(userId, pairList);
        count += 1;
    }

    public List<Integer> getNewsFeed(int userId) {
        List<Integer> res = new ArrayList<>();
        maxHeap = new PriorityQueue<>((o1, o2) -> o2.getKey().getKey().compareTo(o1.getKey().getKey()));

        Set<Integer> set = followMap.getOrDefault(userId, new HashSet<>());
        set.add(userId);
        followMap.put(userId, set);
        for (int followeeId: followMap.get(userId)) {
            if (tweetMap.containsKey(followeeId)) {
                int index = tweetMap.get(followeeId).size() - 1;
                Pair<Integer, Integer> pair = tweetMap.get(followeeId).get(index);
                Pair<Pair<Integer, Integer>, Pair<Integer, Integer>> quad = new Pair<>(
                        pair,
                        new Pair<>(followeeId, index - 1)
                );
                maxHeap.add(quad);
            }
        }

        while (!maxHeap.isEmpty() && res.size() < 10) {
            Pair<Pair<Integer, Integer>, Pair<Integer, Integer>> quad = maxHeap.poll();
            res.add(quad.getKey().getValue());
            int index = quad.getValue().getValue();
            if (index >= 0) {
                int followeeId = quad.getValue().getKey();
                Pair<Integer, Integer> pair = tweetMap.get(followeeId).get(index);
                quad = new Pair<>(
                        pair,
                        new Pair<>(followeeId, index - 1)
                );
                maxHeap.add(quad);
            }
        }

        return res;
    }

    public void follow(int followerId, int followeeId) {
        Set<Integer> set = followMap.getOrDefault(followerId, new HashSet<>());
        set.add(followeeId);
        followMap.put(followerId, set);
    }

    public void unfollow(int followerId, int followeeId) {
        if (followMap.getOrDefault(followerId, new HashSet<>()).contains(followeeId)) {
            Set<Integer> set = followMap.get(followerId);
            set.remove(followeeId);
            followMap.put(followerId, set);
        }
    }

    public static void main(String[] args) {
        Twitter twitter = new Twitter();
        twitter.postTweet(1, 5);
        System.out.println(twitter.getNewsFeed(1));
    }
}
