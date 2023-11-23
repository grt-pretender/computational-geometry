# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, 
# append the additional letters onto the end of the merged string.
# Return the merged string.

def mergeAlternately(word1: str, word2: str) -> str:

	# using two pointers, one for each string
	# O (n + m)
	i, j = 0, 0
	storing_array = []

	while i < len(word1) and j < len(word2):
		storing_array.append(word1[i])
		storing_array.append(word2[j])
		i += 1 
		j += 1
	
	# appends nothing if i/j is out of bounds
	storing_array.append(word1[i:])
	storing_array.append(word2[j:])

	merged_string = "".join(storing_array)
	return merged_string
        

word1, word2 = "ab", "pqrs" 
test = mergeAlternately(word1, word2)
print(test)