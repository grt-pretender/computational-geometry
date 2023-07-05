# Given two strings s and goal, return true 
# if you can swap two letters in s so the result is equal to goal, 
# otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) 
# such that i != j and swapping the characters at s[i] and s[j].

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

      # ===============================================================
      # using Counter 

      # Conditions for True:
      # equal length of these strings,
      # certain number of elements to be different: two or none
      # ===============================================================

      counter1, counter2 = Counter(s), Counter(goal)

      if counter1 != counter2:
        return False
      
      diff = sum([1 for i in range(len(s)) if s[i] != goal[i]])

      if diff == 2:
        return True
      elif diff == 0:
        return any([count > 1 for char, count in counter1.items()])
      else:
        return False
