"""
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""
class Solution(object):
    def reverseWords(self, s):
        result = ''
        for i in s.split():
            result+=i[::-1]+' '
        return result[:-1]

