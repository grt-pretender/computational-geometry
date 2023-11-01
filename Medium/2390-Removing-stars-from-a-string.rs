// You are given a string s, which contains stars *.

// In one operation, you can:
// Choose a star in s.
// Remove the closest non-star character to its left, as well as remove the star itself.
// Return the string after all stars have been removed.

// using stack and regex

impl Solution {
    pub fn remove_stars(s: String) -> String {
        let new_s = s.chars().collect::<Vec<char>>();
        let mut storing = String::new();
        let pattern = String::from("*");

        for char in &new_s {
            if char.to_string() == pattern.to_string() {
                storing.pop();
            } else {
                storing.push(*char);
            }
        }
        storing
    }
}
