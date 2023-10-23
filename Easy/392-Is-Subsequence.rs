// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string
// by deleting some (can be none) of the characters without disturbing the relative positions
// of the remaining characters.
// (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        // using two pointers
        let (mut i, mut j) = (0, 0);
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();

        while i < s.len() && j < t.len() {
            if s[i] == t[j] {
                i += 1;
            }
            j += 1;
        }
        i == s.len()
    }
}
