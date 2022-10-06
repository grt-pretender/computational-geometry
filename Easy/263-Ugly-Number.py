# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.


class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        
        for prime_number in [2, 3, 5]:

            while n % prime_number == 0:
                n = n // prime_number
        
        return n == 1




