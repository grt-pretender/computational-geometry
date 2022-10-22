# You are climbing a staircase. 
# It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# ==========================

# using dynamic programming, memorization, bottom-up approach 
# using two pointers, each step capacity is the sum of the two previous ones, 
# like Fibonacci numbers


class Solution:
    def climbStairs(self, n: int) -> int:
        
        first_pointer = 1
        second_pointer =  1

        for i in range(n - 1):
            temporary = first_pointer
            first_pointer = first_pointer + second_pointer
            second_pointer = temporary

        return first_pointer


