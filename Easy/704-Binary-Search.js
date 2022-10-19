// Given an array of integers nums
// which is sorted in ascending order,
// and an integer target,
// write a function to search target in nums.

// If target exists, then return its index.
// Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.

var search = function(nums, target) {
        
        // using two pointers
        var left_pointer = 0;
        var right_pointer = nums.length - 1;

        while (left_pointer <= right_pointer) {
            var middle_point = right_pointer - left_pointer / 2;

            if (nums[middle_point] < target) {
                left_pointer = middle_point + 1;
            } 
            else if (nums[middle_point] > target) {
                right_pointer = middle_point - 1;
            } 
            else {
                return middle_point;
            }
        }

        return -1;
    
};


