// The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
// such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
// Given n, calculate F(n).

/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {

// ============================================
// 1) Using recursion
// ============================================

    if (n <= 1) 
        return n;
    
    return fib(n-1)+fib(n-2);
    
};
     

// ============================================
// 2) Using dynamic programming and memoization
// ============================================

var fib = function(n) {

    let memo = new Array(n+2);
    memo[0] = 0;
    memo[1] = 1;
                
    if (n in memo)
        return memo[n];
        
    else {
        for (let k = 2; k <= n; k++) {
            memo[k] = memo[k-1] + memo[k-2];
            } 
        return memo[n];
        }   
};



