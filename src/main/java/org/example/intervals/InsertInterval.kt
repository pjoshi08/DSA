package org.example.intervals

import kotlin.math.max
import kotlin.math.min

fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
    /*intervals.sortedWith(
        compareBy<IntArray> { it[0] }
            .thenBy { it[1] }
    )*/  // Intervals are already sorted in this question
    val res = mutableListOf<IntArray>()
    var newInterval = newInterval
    for (i in intervals.indices) {
        if (newInterval[1] < intervals[i][0]) {
            res.add(newInterval)
            return (res + intervals.slice(i..<intervals.size)).toTypedArray()
        } else if (intervals[i][1] < newInterval[0]) {
            res.add(intervals[i])
        } else {
            newInterval = intArrayOf(
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            )
        }
    }
    res.add(newInterval)
    return res.toTypedArray()
}

fun insert2(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
    val res = mutableListOf<IntArray>()

    var start = newInterval[0]
    var end = newInterval[1]
    var counter = 0

    while (counter < intervals.size && intervals[counter][1] < start)
        res.add(intervals[counter++])

    while (counter < intervals.size && intervals[counter][0] <= end) {
        start = min(intervals[counter][0], start)
        end = max(intervals[counter++][1], end)
    }

    res.add(intArrayOf(start, end))

    while (counter < intervals.size)
        res.add(intervals[counter++])

    return res.toTypedArray()
}