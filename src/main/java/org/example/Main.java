package org.example;

import org.example.arrays.GroupAnagrams;
import org.example.arrays.LongestConsecutiveInts;
import org.example.arrays.ProductArrayExceptSelf;
import org.example.arrays.ValidSudoku;
import org.example.binarysearch.BinarySearch;
import org.example.binarysearch.RotatedArrSearch;
import org.example.binarysearch.Search2DMatrix;
import org.example.blind.MergeIntervals;
import org.example.blind.RevLinkedList;
import org.example.stack.CarFleet;
import org.example.stack.DailyTemps;
import org.example.stack.GenerateParentheses;
import org.example.twopointers.ThreeSum;
import org.example.twopointers.TwoSumII;
import org.example.twopointers.ValidPalindrome;
import org.example.twopointers.WaterContainer;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        RotatedArrSearch obj = new RotatedArrSearch();
        int[] nums = {1, 3};
        int[] speed = {4,2,1};
        //int[][] nums = {{1,3,5,7}, {10,11,16,20}, {23,30,34,60}, };

        System.out.println(obj.search(nums, 1));

    }
}