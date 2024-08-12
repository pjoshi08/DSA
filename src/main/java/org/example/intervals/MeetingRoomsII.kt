package org.example.intervals

fun minMeetingRooms(intervals: Array<IntArray>): Int {
    val start = intervals.map { it[0] }.sorted()
    val end = intervals.map { it[1] }.sorted()
    var s = 0; var e = 0
    var count = 0; var res = 0
    while (s < intervals.size) {
        if (start[s] < end[e]) {
            count += 1
            s += 1
        } else {
            count -= 1
            e += 1
        }
        res = if (count > res) count else res
    }

    return res
}