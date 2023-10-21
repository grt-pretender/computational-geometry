# Given an array of integers nums, sort the array in ascending order and return it.

import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # using heap sort
        heapq.heapify(nums)
        stored = []
        
        for i in range(0, len(nums)):
            stored.append(heapq.heappop(nums))

        return stored