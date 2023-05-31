// Task: Given an integer array nums,
// return true if any value appears at least twice in the array,
// and return false if every element is distinct.

use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut our_hashset = HashSet::new();
        for &number in nums.iter() {
            if our_hashset.contains(&number) {
                return true;
            }

            our_hashset.insert(number);
        }

        return false;
    }
}
