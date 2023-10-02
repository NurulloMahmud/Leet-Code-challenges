"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

https://leetcode.com/problems/reverse-integer/description/
"""

class Solution(object):
    def reverse(self, x):
        # reverse the x by converting it to str
        x = str(x)[::-1]
        # if x was less than 0, convert the str to int by multiplying -1
        if '-' in x:
            x = -1*int(x[:-1])
        # convert the type of x back to int
        x=int(x)
        # check if the x in size of 32-bit
        if x > (2**31-1) or x < (-2**31+1) or x == 0:
            return 0
        return x
    
# Runtime: Beats 67.40%of users with Python
# Memory: Beats 47.13%of users with Python