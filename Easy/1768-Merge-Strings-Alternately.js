// You are given two strings word1 and word2.
// Merge the strings by adding letters in alternating order, starting with word1.
// If a string is longer than the other,
// append the additional letters onto the end of the merged string.
// Return the merged string.


/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {

	// using one pointer and the max length of these strings
    let res = [];
    maxLen = Math.max(word1.length, word2.length);

    for (i = 0; i < maxLen; i++) {
        word1[i] && res.push(word1[i]);
        word2[i] && res.push(word2[i]);
    }
    return res.join('');
}


