// An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

// Given an integer n, return true if n is an ugly number.

impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        let mut our_number = n;

        if our_number <= 0 {
            return false;
        }

        for prime_number in [2, 3, 5] {
            while our_number % prime_number == 0 {
                our_number = our_number / prime_number;
            }
        }

        our_number == 1
    }
}
