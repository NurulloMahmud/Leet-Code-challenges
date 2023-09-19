class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [i for i in s]
        characters=[]
        characters_lenths=[]
        for c in letters:
            if c in characters:
                indx_of_av_char = characters.index(c)
                characters_lenths.append(len(characters))
                characters = characters[indx_of_av_char+1:]
                print(characters)
            characters.append(c)
        if len(characters)>0:

            return max(characters_lenths)
        print(characters)
        return 0
    