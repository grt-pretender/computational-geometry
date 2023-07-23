// You are given an integer array height of length n.
// There are n vertical lines drawn such that the two endpoints of the ith line are
// (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container,
// such that the container contains the most water.

// Return the maximum amount of water a container can store.
// Notice that you may not slant the container.

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let (mut our_result, mut left_ptr, mut calculated_area) = (0, 0, 0);
        let mut right_ptr = height.len() - 1;

        while left_ptr < right_ptr {
            calculated_area =
                (right_ptr - left_ptr) as i32 * core::cmp::min(height[left_ptr], height[right_ptr]);
            our_result = core::cmp::max(our_result, calculated_area);

            if height[left_ptr] < height[right_ptr] {
                left_ptr += 1
            } else {
                right_ptr -= 1
            }
        }

        our_result as i32
    }
}
