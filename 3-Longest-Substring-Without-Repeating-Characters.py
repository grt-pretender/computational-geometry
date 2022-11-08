# Given a string s, find the length 
# of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # using sliding window = two pointers
 
        storing_set = set()
        result = 0
        left = 0
        right = 1

        for right in range(len(s)): 
            
            while s[right] in storing_set:
                storing_set.remove(s[left])
                left += 1

            storing_set.add(s[right])
            result = max(result, right - left + 1)
        
        return result



                
