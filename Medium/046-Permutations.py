# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

# Constraints:
#  1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# using backtracking: to the base cases (single element) and gradually adding up again

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

      answer = []

      if len(nums) == 1:
        base_case = [nums.copy()]
        return base_case

      for i in range(len(nums)):
        n = nums.pop(0)
        our_permutations = self.permute(nums)

        for permutation in our_permutations:
          permutation.append(n)
        answer.extend(our_permutations)
        nums.append(n)

      return answer
