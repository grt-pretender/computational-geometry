// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
// determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

use std::collections::HashMap;
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut our_stack = Vec::new();
        let mut closing_and_opening = HashMap::from([(')', '('), ('}', '{'), (']', '[')]);

        for c in s.chars() {
            if closing_and_opening.contains_key(&c) {
                if our_stack.iter().last() == closing_and_opening.get(&c) {
                    our_stack.pop();
                } else {
                    return false;
                }
            } else {
                our_stack.push(c)
            }
        }

        our_stack.is_empty()
    }
}
