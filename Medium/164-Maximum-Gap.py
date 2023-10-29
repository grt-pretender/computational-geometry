# Given an integer array nums, return the maximum difference 
# between two successive elements in its sorted form. 
# If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
    	    return 0
        else:
            sorted_nums = sorted(nums) 
            curr_diff, max_diff = 0, 0
            
            for i in range(0, len(sorted_nums)):
                curr_diff = sorted_nums[i] - sorted_nums[i - 1]
                max_diff = max(max_diff, curr_diff)
            return max_diff

      
