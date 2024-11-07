# A sentence is a list of words that are separated by a single space 
# with no leading or trailing spaces.

# Words consist of only uppercase and lowercase English letters. 
# Uppercase and lowercase English letters are considered different.

# A sentence is circular if:
# - The last character of a word is equal to the first character of the next word.
# - The last character of the last word is equal to the first character of the first word.

# Task: Given a string sentence, return true if it is circular. Otherwise, return false.

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
    	
# ====================================================
# 1) Extra memory required
# ====================================================

        words = sentence.split(" ")
        for i in range(len(words)):
            if words[i][0] != words[i-1][-1]:
                return False
        return True

# =====================================================
# 2) Find another space, then compare two letters
# Edge case: when there is only one word
# =====================================================

        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i-1] != sentence[i+1]:
                return False
        return sentence[0] == sentence[-1]
