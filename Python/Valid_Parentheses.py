"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

https://leetcode.com/problems/valid-parentheses/description/
"""

# we use stack algorithm  

class Solution:
    def isValid(self, s: str) -> bool:
        # storing the opening brackets
        stack=[]
        pairs = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in pairs.values():
                stack.append(i)
            if i in '}])':
                # check if last element before i was opening of the i
                if not stack or stack[-1]!=pairs[i]:
                    return False
                stack.pop()

        return not stack
