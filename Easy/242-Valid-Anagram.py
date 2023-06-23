# Given two strings s and t, return true 
# if t is an anagram of s, and false otherwise.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# =================================
# 1)  Using build-in sorting method
# =================================
        
        string1 = sorted(s)
        string2 = sorted(t)
        
        if string1 != string2:
            return False
        return True
        
# =================================
# 2)  Another variant
# =================================
        
        if len(s) != len(t):
            return False

        new_counter = Counter(s)
        for c in t:
            new_counter[c] -= 1
            if new_counter[c] < 0:
                return False
        return True
        
# =================================
# 3)  Neetcode`s hint) 
# =================================

        return Counter(s) == Counter(t)
