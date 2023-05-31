# Task: Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = []
        storing_data = sorted(nums)
        for number in storing_data:
            if number in hashset:
                return True
            hashset.append(number)
        return False


