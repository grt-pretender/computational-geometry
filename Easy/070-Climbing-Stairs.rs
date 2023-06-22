// You are climbing a staircase.
// It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps.
// In how many distinct ways can you climb to the top?

// ==========================

// using dynamic programming, memorization, bottom-up approach
// solving a recursive problem iteratively
// using two pointers, each step capacity is the sum of the two previous ones,
// like Fibonacci numbers

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut first_pointer: i32 = 1;
        let mut second_pointer: i32 = 1;

        for i in 0..n - 1 {
            let mut temporary = first_pointer;
            first_pointer = first_pointer + second_pointer;
            second_pointer = temporary;
        }

        return first_pointer;
    }
}
