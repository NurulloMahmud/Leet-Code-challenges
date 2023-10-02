"""
1021. Remove Outermost Parentheses
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

https://leetcode.com/problems/remove-outermost-parentheses/description/
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        queue_ = '' # stores opening parenthesis
        stack = '' # stores closing parenthesis
        result = '' # stores inner parenthesis
        temp = ''   # stores everything until we find both opening and closing parenthesis
        for i in s:
            if i=='(':
                queue_+=i
            elif i==')':
                stack+=i
            temp+=i
            # if both opening and closing parenthesis have same length and it's not 0, we reached the outer parenthesis
            if len(queue_) == len(stack) and len(queue_) != 0:
                # store inner and disregard outers
                result+=temp[1:-1]
                temp=''
        return result

a=Solution()
print(a.removeOuterParentheses("(()())(())(()(()))"))