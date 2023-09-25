"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

https://leetcode.com/problems/valid-parentheses/description/
"""

# we use stack algorithm  

class Solution:
    def isValid(self, s: str) -> bool:
        # storing the opening brackets
        opened=[]
        pairs = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in pairs.values():
                opened.append(i)
            if i in '}])':
                # check if last element before i was opening of the i
                if not opened or opened[-1]!=pairs[i]:
                    return False
                opened.pop()

        return not opened

a=Solution()
print(a.isValid('({[}])'))