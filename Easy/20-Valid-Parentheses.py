# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:

        our_stack = [] 
        closing_and_opening = { 
        ")" : "(",
        "}" : "{",
        "]" : "["
        }

        for c in s:
            if c in closing_and_opening:
                
        #  matching open/close parenthesis usinig c as a key in our hashmap
                if our_stack and our_stack[-1] == closing_and_opening[c]:
                    our_stack.pop()
                else:
                    return False

            else:
                our_stack.append(c)

        # if our stack is empty - all pairs are matched and the string is valid  
        return True if not our_stack else False



