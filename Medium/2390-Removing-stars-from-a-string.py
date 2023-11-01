# You are given a string s, which contains stars *.

# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# using stack and regex

import re

def removeStars(s: str) -> str:

    pattern = r"*"
    storing = []

    for char in s:
   
        if char not in pattern:
            storing.append(char)
        else:
            storing and storing.pop()

    return "".join(storing)
    

s = "leet**cod*e"
print(removeStars(s))

