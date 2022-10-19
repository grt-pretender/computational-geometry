// Given an array of integers nums
// which is sorted in ascending order,
// and an integer target,
// write a function to search target in nums.

// If target exists, then return its index.
// Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        // using two pointers

        let mut size = nums.len();
        let mut left_pointer = 0;
        let mut right_pointer = size as i32 - 1;

        while left_pointer <= right_pointer {
            let middle_point = right_pointer - left_pointer / 2;

            if nums[middle_point as usize] < target {
                left_pointer = middle_point + 1;
            } else if nums[middle_point as usize] > target {
                right_pointer = middle_point - 1;
            } else {
                return middle_point as i32;
            }
        }

        return -1;
    }
}
