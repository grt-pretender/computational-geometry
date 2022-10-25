// You are climbing a staircase.
// It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps.
// In how many distinct ways can you climb to the top?


/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    var our_array = [] 
    our_array[1] = 1;
    our_array[2] = 2;
    
    for (let i=3; i<=n; i++) {
        our_array[i] = our_array[i-1] + our_array[i-2]
        }

    return our_array[n];
    
};



