"""
1614. Maximum Nesting Depth of the Parentheses
Given a VPS represented as string s, return the nesting depth of s.

https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        # we use stack data structure
        stack = []
        # if input doesn't include paranthesis return 0
        l = [0] # store length of opening paranthesis
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')':
                l.append(len(stack))
                stack.pop()
        return max(l)
