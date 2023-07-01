//Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
//find the one that is missing from the array.

//using Gauss' formula: n(n+1)/2

impl Solution {
    
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        
        let n = nums.len() as i32;
        let nums_sum: i32 = nums.iter().sum();
        let n_total_sum: i32 = n * (n + 1) / 2;
        let result = n_total_sum - nums_sum;
        result
    } 
}

