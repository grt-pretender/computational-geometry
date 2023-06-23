# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

        
# ========================================
# 1) Using build-in functions
# ========================================

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        input_data = s.strip().split(" ")
        return len(input_data[-1])

# ========================================
# 2) searching from the end of the string 
#    (for one word only)
# ========================================

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        pointer, length = len(s) - 1, 0

        while s[pointer] == " ":
            pointer -= 1
        while pointer >= 0 and s[pointer] != " ":
            length +=1
            pointer -= 1
        return length






 
