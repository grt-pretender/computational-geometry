// You are given an integer array height of length n. 
// There are n vertical lines drawn such that the two endpoints of the ith line are 
// (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container, 
// such that the container contains the most water.

// Return the maximum amount of water a container can store.
// Notice that you may not slant the container.


import "math"

func maxArea(height []int) int {

    left_ptr := 0
    right_ptr := len(height) - 1
    var our_result float64 = 0
    var calculated_area float64 = 0

    for left_ptr < right_ptr {
        calculated_area = float64(right_ptr - left_ptr) * math.Min(float64(height[left_ptr]), float64(height[right_ptr]))
        our_result = math.Max(our_result, calculated_area)

        if height[left_ptr] < height[right_ptr] {
            left_ptr += 1
        } else {
            right_ptr -= 1
        }
    }
    
    return int(our_result)
    
}