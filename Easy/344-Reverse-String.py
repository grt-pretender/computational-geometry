# Write a function that reverses a string. 
# The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:

# ===================================================================
# 1) using two pointers to iterate through the string and swap values     
# ===================================================================
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            left_pointer += 1
            right_pointer -= 1


# ===================================================================
# 2) using stack and one pointer, 'first in - last out" approach
# ===================================================================

        storing_place = []
        pointer = 0

        for character in s:
            storing_place.append(character)

        while storing_place:
            s[pointer] = storing_place.pop()
            pointer += 1
            

# ===================================================================
# 3) using recursion
# ===================================================================

        def reverse_string(left_pointer, right_pointer):

            if left_pointer < right_pointer:
                s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
                reverse_string(left_pointer + 1, right_pointer - 1)
            
        reverse_string(0, len(s) - 1)

