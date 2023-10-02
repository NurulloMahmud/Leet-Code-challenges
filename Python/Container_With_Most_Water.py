"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""

class Solution(object):
    def maxArea(self, height):
        forwards, backwards = 0, len(height)-1
        capacities = []

        while backwards > forwards:
            if height[backwards] < height[forwards]:
                area = height[backwards] * (backwards-forwards)
                capacities.append(area)
                backwards -= 1
            elif height[backwards] > height[forwards]:
                area = height[forwards] * (backwards-forwards)
                capacities.append(area)
                forwards += 1
            else:
                area = height[forwards] * (backwards-forwards)
                capacities.append(area)
                forwards += 1; backwards-=1
        return max(capacities)
