# Given a sentence text (A sentence is a string of space-separated words) in the following format:

# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that 
# all words are rearranged in an increasing order of their lengths. 
# If two words have the same length, arrange them in their original order.

# Return the new text following the format shown above.


def arrangeWords(text: str) -> str:
	text = text.split()
	sorted_text = sorted(text, key=len)
	return " ".join(sorted_text).capitalize()

        
text = "Leetcode is cool"
print(arrangeWords(text))