// Given an array of integers nums, sort the array in ascending order and return it.

use std::collections::BinaryHeap;
impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        // using heap sort
        let mut temp_vec = Vec::new();
        let mut stored = Vec::new();
        let mut heap = BinaryHeap::from(nums);

        for _val in heap.clone().into_iter() {
            temp_vec.push(heap.pop());
        }
        temp_vec.reverse();

        for el in &temp_vec {
            stored.push(el.unwrap());
        }

        stored
    }
}
