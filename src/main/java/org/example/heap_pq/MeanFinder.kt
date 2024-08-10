package org.example.heap_pq

import java.util.*

class MedianFinder() {

    private val large: PriorityQueue<Int> = PriorityQueue()
    private val small: PriorityQueue<Int> = PriorityQueue(Collections.reverseOrder())
    var len: Int = 0

    fun addNum(num: Int) {
        /*
        If the number I am inserting is larger than the
        largest value in the smaller heap (the top value),
        then it should go in the larger heap.
         Otherwise it does in the smaller heap
        */
        if (large.size > 0 && num > small.peek()) {
            large.add(num)
        } else {
            small.add(num)
        }

        /*
        Now the values are divided into the
        larger and smaller heaps appropriately
        but we need to check if one is too big.

        Each heap has to have the same amount, or
        the one of them can be consistently can be 1 bigger
        (in this case I chose the smaller heap
        to be allowed to be 1 bigger).
        If the larger heap has more values, smallest
        value of the larger heap (the top of the heap)
        needs to be moved to the smaller heap to
        maintain the correct size for each.
        */

        if (small.size < large.size) {
            small.add(large.poll())
        } else if (small.size > large.size + 1) {
            large.add(small.poll())
        }
        len += 1
    }

    fun findMedian(): Double {
        return if (len % 2 == 0) {
            (large.peek() + small.peek()).toDouble() / 2
        } else {
            small.peek().toDouble()
        }
    }

}