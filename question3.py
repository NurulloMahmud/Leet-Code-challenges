# 3. Longest Substring Without Repeating Characters

"""
Given a string s, find the length of the longest 
substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [i for i in s]    # getting every letter in a string
        characters=[]   # stores unique characters
        characters_lenths=[]    # stores the length of unique characters only

        for c in letters:
            if c in characters: # if the letter already exists in a sub string, do the followings
                indx_of_av_char = characters.index(c)   # get the index of existing character in a sub string 
                characters_lenths.append(len(characters))   # store the length of this unique sub string
                characters = characters[indx_of_av_char+1:] # get rid of the part of sub string to make it unique when the current letter is added
            characters.append(c)    
        characters_lenths.append(len(set(characters)))  # store the last sub string's length

        return max(characters_lenths)

test=Solution()
print(test.lengthOfLongestSubstring(input("input a string/word to test: ")))