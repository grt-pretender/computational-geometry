// Given a string s consisting of words and spaces,
// return the length of the last word in the string.
// A word is a maximal substring consisting of non-space characters only.

// ========================================
// Using build-in functions
// ========================================

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let input_data = s.trim().split(" ").last().unwrap();
        return input_data.len() as i32;
    }
}
