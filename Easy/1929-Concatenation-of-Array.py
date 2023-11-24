# 1929. Concatenation of Array

# Given an integer array nums of length n, 
# you want to create an array ans of length 2n 
# where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

def getConcatenation(nums: list[int]) -> list[int]:

	# 1) iterating through an array
	
	for i in range(0, len(nums)):
		nums.append(nums[i]) 	
	return nums


	# 2) creating an extra array
	ans = []
	for i in range(2):
		for v in nums:
			ans.append(v) 	
	return ans


	# 3) creating an extra array, another option
    	n = len(nums)
    	ans = [0]*2*n
	
    	for i in range(0, n):
      	ans[i] = nums[i]
      	ans[i+n] = nums[i]
    	return ans


	# 4) and another one
	return nums*2

nums = [1,3,2,1]
print(getConcatenation(nums))
