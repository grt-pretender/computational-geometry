// Write a function that reverses a string. 
// The input string is given as an array of characters s.
// You must do this by modifying the input array in-place with O(1) extra memory.


// ===================================================================
// using two pointers to iterate through the string and swap values     
// ===================================================================

func reverseString(s []byte)  {
    var left_pointer = 0
    var right_pointer = len(s) - 1
    
    for left_pointer < right_pointer {
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        left_pointer += 1
        right_pointer -= 1
    }
}

