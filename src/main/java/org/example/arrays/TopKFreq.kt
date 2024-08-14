package org.example.arrays

fun topKFrequent(nums: IntArray, k: Int): IntArray {
    val n = nums.size
    val buckets = Array(n + 1) { mutableListOf<Int>() }  // no 0 freq bucket, num appears at least once
    val count = mutableMapOf<Int, Int>()

    for (num in nums) {
        count[num] = 1 + (count[num] ?: 0)
    }

    for ((num, cnt) in count) {
        buckets[cnt].add(num)
    }

    val res = mutableListOf<Int>()
    for (i in buckets.size - 1 downTo 1) {
        for (num in buckets[i]) {
            res.add(num)
            if (res.size == k) {
                return res.toIntArray()
            }
        }
    }
    return res.toIntArray()
}