from math import sqrt
from typing import List


class Solution:
    # Greedy solution, O(n)
    # we try to minimize each element as we don't know
    # the elements on the right as we go from left to right
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            # we do not check for n < 2 because we find
            # prime between 2 - upper_bound - 1
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0: return False
            return True

        prev = 0
        for n in nums:
            upper_bound = n - prev  # non inclusive

            largest_p = 0
            for i in reversed(range(2, upper_bound)):
                if is_prime(i):
                    largest_p = i
                    break

            # If this is true, that means we cannot create
            # strictly increasing arr
            if n - largest_p <= prev:
                return False
            prev = n - largest_p

        return True

    # O(n * m + m * sqrt(m))
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            # we do not check for n < 2 because we find
            # prime between 2 - upper_bound - 1
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0: return False
            return True

        primes = [False, False]  # True if ith index value is prime
        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(True)
            else:
                primes.append(False)

        prev = 0
        for n in nums:
            upper_bound = n - prev  # non inclusive

            largest_p = 0
            for i in reversed(range(2, upper_bound)):
                if primes[i]:
                    largest_p = i
                    break

            # If this is true, that means we cannot create
            # strictly increasing arr
            if n - largest_p <= prev:
                return False
            prev = n - largest_p

        return True

    # O(n + m * sqrt(m))
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            # we do not check for n < 2 because we find
            # prime between 2 - upper_bound - 1
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0: return False
            return True

        # pre-compute primes
        primes = [0, 0]  # largest prime < ith index value
        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i - 1])

        prev = 0
        for n in nums:
            upper_bound = n - prev  # non inclusive

            largest_p = primes[upper_bound - 1]

            # If this is true, that means we cannot create
            # strictly increasing arr
            if n - largest_p <= prev:
                return False
            prev = n - largest_p

        return True
