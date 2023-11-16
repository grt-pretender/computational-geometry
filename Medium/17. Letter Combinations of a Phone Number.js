// Given a string containing digits from 2-9 inclusive, 
// return all possible letter combinations that the number could represent. 
// Return the answer in any order.
// Note that 1 does not map to any letters.

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    var res = [];
    var forStoring = []; 
    var allDigits = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    };

    // using dfs for all combinations
    var dfs = (i, digits, forStoring) => {
        if (digits === '') return [];
        
        if (i == digits.length) {
            res.push(forStoring.join(''));
            return;
        } 

        let chars = allDigits[digits[i]];
        for (let char of chars) {
            forStoring.push(char);
            dfs(i+1, digits, forStoring);
            forStoring.pop();
            }
        };

    dfs(0, digits, []);
    return res;
    
};