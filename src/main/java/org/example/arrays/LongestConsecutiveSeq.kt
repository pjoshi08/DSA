package org.example.arrays

fun longestConsecutive(nums: IntArray): Int {
    val numSet = nums.toSet()
    var longest = 0

    for (n in nums) {
        if ((n - 1) !in numSet) {  // identify start of sequence
            var length = 0
            while ((n + length) in numSet) {
                length++
            }
            longest = maxOf(longest, length)
        }
    }
    return longest
}