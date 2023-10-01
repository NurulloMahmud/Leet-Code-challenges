"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
https://leetcode.com/problems/3sum/description/
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets={} # keeps unique triplets as keys
        nums.sort()
        # iterate through array till index -2
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                # skip duplicate elements
                continue
        
            left = i + 1    # iterate from current i+1 till right
            right = len(nums) - 1 # come from end to left 

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    # if triplets found add them to dictionary as keys
                    triplets[(nums[i], nums[left], nums[right])]=None
                    left+=1
                    right-=1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        result = [list(i) for i in triplets.keys()]
        return result


