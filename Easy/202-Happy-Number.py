# Starting with any positive integer, replace the number 
# by the sum of the squares of its digits.

# Repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1.

# Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        
        storage_set = set()

        while n not in storage_set:
            storage_set.add(n)
            n = self.sumOfSquares(n)

            if n == 1:        #our happy number!
                return True
        
        return False


    def sumOfSquares(self, n: int) -> int:

    # number % 10 - > to find the last digit
    # number // 10 - > to drop the last digit and go to the next one 
    
        output = 0

        while n != 0:
            digit = n % 10
            digit = digit ** 2
            output += digit
            digit // 10 

        return output
