# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

# =================================
# 1)  Using build-in counter
# =================================

# get top k frequent elements using collections.Counter and heapq.nlargest()

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    	from collections import Counter

    	if len(nums) == k:
    		return nums

    	my_counter = Counter(nums)
    	answer = heapq.nlargest(k, my_counter.keys(), key=my_counter.get)
    	return answer


# =================================
# 2)  Using bucket sort algorithm
# =================================

# 1) iterate through nums, count occurencies of each element, store in a new hasmap my_count (element : count).
# 2) sort data using bucket sort algorithm:
# 2.1) make a limited my_freq_array where index = frequency and value = elements with this frequency,
# array limit: len(nums) + 1;
# 2.2) start the search from the end of this array where the most frequent elements are;
# 2.3) use separate variable answer for storing top frequent elements;
# 2.4) when len(answer) == k, return result.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    	my_count = {}
    	my_freq_array = [[] for i in range(len(nums) + 1)]

    	for n in nums:
    		my_count[n] = 1 + my_count.get(n, 0)

    	for n, c in my_count.items():
    		my_freq_array[c].append(n)

    	answer = []

    	for i in range(len(my_freq_array) - 1, 0, -1):
    		for n in my_freq_array[i]:
    			answer.append(n)

    			if len(answer) == k:
    				return answer


