# You are given a string s and an integer k. 
# You can choose any character of the string and change it
# to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter 
# you can get after performing the above operations.

# ====================
# using sliding window
# to maximize result we have to change less frequent elements
# Thus, we can use the difference between the length of the sliding window 
# and max count for the most frequent element in the string
# this difference shouldn`t exceed k

# when to update the right pointer - always by default, cause it`s an iteration by index
# when to update the left pointer - only if the difference is bigger than k 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table_for_count = {}
        left_ptr, our_result = 0, 0

        for right_ptr in range(len(s)):
            
            table_for_count[s[right_ptr]] = 1 + table_for_count.get(s[right_ptr], 0)
            sliding_window = right_ptr - left_ptr + 1 
            
            if sliding_window - max(table_for_count.values()) > k:
                table_for_count[s[left_ptr]] -= 1
                left_ptr += 1
            
            sliding_window = right_ptr - left_ptr + 1    
            our_result = max(our_result, sliding_window)

        return our_result