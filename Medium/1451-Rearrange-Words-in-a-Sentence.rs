// Given a sentence text (A sentence is a string of space-separated words) in the following format:

// First letter is in upper case.
// Each word in text are separated by a single space.
// Your task is to rearrange the words in text such that
// all words are rearranged in an increasing order of their lengths.
// If two words have the same length, arrange them in their original order.

// Return the new text following the format shown above.

impl Solution {
    pub fn arrange_words(text: String) -> String {
        let binding = text.to_lowercase();
        let mut iter: Vec<_> = binding.split(" ").collect();
        iter.sort_by_key(|k| k.len());

        let mut new_string = Vec::new();
        new_string.extend(iter);

        let mut ans = new_string.join(",").replace(",", " ");
        if !ans.is_empty() {
            ans[0..1].make_ascii_uppercase()
        }
        ans
    }
}
