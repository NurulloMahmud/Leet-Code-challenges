
"""
13. Roman to Integer
Given a roman numeral, convert it to an integer.

https://leetcode.com/problems/roman-to-integer/description/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }

        total = 0
        prev_value = 0  # Keep track of the previous symbols value

        # Iterate through the string in reverse order
        for char in reversed(s):
            value = roman[char]
            if value < prev_value:
                total -= value  # Subtract if the current symbol is smaller than the previous one
            else:
                total += value
            prev_value = value

        return total
