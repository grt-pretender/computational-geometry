
#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
#find the one that is missing from the array.

#using Gauss' formula: n(n+1)/2


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n_total_sum = int(n * (n + 1) / 2)
        nums_sum = sum(nums) 
        result = n_total_sum - nums_sum
        return result


