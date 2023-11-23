// You are given two strings word1 and word2.
// Merge the strings by adding letters in alternating order, starting with word1.
// If a string is longer than the other,
// append the additional letters onto the end of the merged string.
// Return the merged string.

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        // using one pointer and the max length of these strings
        let mut word1 = word1.as_bytes();
        let mut word2 = word2.as_bytes();
        let mut i = 0;
        let mut storing_array = Vec::new();
        let max_len = word1.len().max(word2.len());

        for i in 0..max_len {
            if word1.get(i).is_some() {
                storing_array.push(word1[i]);
            }
            if word2.get(i).is_some() {
                storing_array.push(word2[i]);
            }
        }

        let merged_string = String::from_utf8(storing_array).unwrap();
        return merged_string;
    }
}
