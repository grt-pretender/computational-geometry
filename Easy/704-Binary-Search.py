# Given an array of integers nums 
# which is sorted in ascending order, 
# and an integer target, 
# write a function to search target in nums. 

# If target exists, then return its index. 
# Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # using two pointers
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:

            middle_point = right_pointer - left_pointer // 2
            
            if nums[middle_point] < target:
                left_pointer = middle_point + 1
            elif nums[middle_point] > target:
                right_pointer = middle_point - 1
            else:
                return middle_point

        return -1







 