# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:

# ============================================
 1) Using recursion
# ============================================

        if n <= 1: 
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
     

# ============================================
# 2) Using dynamic programming and memoization
# ============================================

        memo = [0, 1]
        
        if n == 0:
            return memo[0]
        elif n == 1:
            return memo[1]
                
        elif n in memo:
            return memo[n]
        
        else:
            for k in range(2, n+1):
                memo.append(memo[k-1] + memo[k-2])
            return memo[n]
        
        