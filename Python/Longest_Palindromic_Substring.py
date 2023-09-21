"""
5. Longest Palindromic Substring

Given a string s, return the longest 
palindromic


https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # we store all palindromes in a list
        palindromes = []
        temp=''
        # for every letter in a string
        for index, c in enumerate(s):
            temp+=c
            # one more loop that comes from end of string to current letter
            for i in range(len(s)-1, index, -1):
                # if there is a letter similar to first letter in current substring
                if c==s[i]:
                    test=s[index:i+1]
                    # check if if the current sub string is the same when reversed 
                    if test==test[::-1]:
                        # if the sub string is same when reversed, add it to palindromes list, clear the test sub string, break the inner loop
                        palindromes.append(test)
                        test=''
                        break
        # check if there is a palindrome sub string
        if len(palindromes)>0:
            # sort the list by length of the items
            palindromes=sorted(palindromes, key=len)
            return palindromes[-1]  # return the last item in list that sorted by length of items
        # if given string was not empty and there was no palindrome, return the first/only character in s
        if len(s)>0:
            return s[0]
        # return given s if it was empty
        return s