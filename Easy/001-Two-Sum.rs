// Given an array of integers nums and an integer target,
// return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.
// You can return the answer in any order.

// 1) brute force approach

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut res = vec![0, 0];

        for (i, first_num) in nums.iter().enumerate() {
            for (j, second_num) in nums.iter().enumerate() {
                if (i < j) && (first_num + second_num == target) {
                    res[0] = i as i32;
                    res[1] = j as i32;
                }
            }
        }
        return res;
    }
}

// 2) using a hashmap (value : index mapping) to check for the second num (difference = target - first num)
// going through nums in one run

use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut res = vec![0, 0];
        let mut hm: HashMap<&i32, i32> = HashMap::new();

        for (i, first_num) in nums.iter().enumerate() {
            let mut second_num = target - first_num;
            if (hm.contains_key(&second_num)) {
                res[0] = i as i32;
                res[1] = hm[&second_num] as i32;
            } else {
                hm.insert(first_num, i as i32);
            }
        }
        return res;
    }
}
