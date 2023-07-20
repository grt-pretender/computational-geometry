// You are given a string s and an integer k.
// You can choose any character of the string and change it
// to any other uppercase English character.
// You can perform this operation at most k times.

// Return the length of the longest substring containing the same letter
// you can get after performing the above operations.

// ====================
// using sliding window
// to maximize result we have to change less frequent elements
// Thus, we can use the difference between the length of the sliding window
// and max count for the most frequent element in the string
// this difference shouldn`t exceed k

// when to update the right pointer - always by default, cause it`s an iteration by index
// when to update the left pointer - only if the difference is bigger than k

use std::collections::HashMap;
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let (mut left_ptr, mut our_result) = (0, 0);
        let mut s: Vec<char> = s.chars().collect();
        let mut frequency: HashMap<char, usize> = HashMap::new();

        for right_ptr in 0..s.len() {
            *frequency.entry(s[right_ptr]).or_default() += 1;

            let max_frequency = frequency.values().max().unwrap();
            let sliding_window = right_ptr - left_ptr + 1;
            let difference = sliding_window - max_frequency;

            if difference > k as usize {
                *frequency.entry(s[left_ptr]).or_default() -= 1;
                left_ptr += 1;
            }

            let sliding_window = right_ptr - left_ptr + 1;
            our_result = core::cmp::max(our_results, sliding_window);
        }
        our_result as i32
    }
}
