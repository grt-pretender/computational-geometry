// Given an integer array nums sorted in non-decreasing order,
// remove the duplicates in-place (Space compl O(1))
// such that each unique element appears only once.

// The relative order of the elements should be kept the same.
// Then return the number of unique elements in nums.

// Consider the number of unique elements of nums to be k,
// to get accepted, you need to do the following things:

// Change the array nums such that the first k elements of nums
// contain the unique elements in the order they were present in nums initially.
// The remaining elements of nums are not important as well as the size of nums.
// Return k.

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        // ========================================================
        // using two pointers going in one direction, left to right
        // the left pointer is also our k
        // ========================================================

        // not 0 cause the fist element will remain where it is
        let mut left_pointer = 1;

        for mut right_pointer in 1..nums.len() {
            // a new unique element is found, and it should be shifted
            if nums[right_pointer] != nums[right_pointer - 1] {
                nums[left_pointer] = nums[right_pointer];

                // updating the left pointer after its cell has been providied with a new unique element
                left_pointer += 1
            }

            // updating the right pointer if two adjacent elements are the same
            right_pointer += 1;
        }

        return left_pointer as i32;
    }
}
