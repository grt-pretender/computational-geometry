# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.



# 1) brute force approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, first_num in enumerate(nums):
            for j, second_num in enumerate(nums[i+1:]):
                if first_num + second_num == target:
                    return [i, j+i+1]


# 2) using a hashmap (value : index mapping) to check for the second num (difference = target - first num)
# going through nums in one run

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}
        for i, first_num in enumerate(nums):
            second_num = target - first_num
            if second_num in hm:
                return [i, hm[second_num]]
            hm[first_num] = i


        