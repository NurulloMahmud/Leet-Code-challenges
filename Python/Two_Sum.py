"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # first algorithm to win in runtime
        num_index = {}
        for i, n in enumerate(nums):
            compliment = target - nums[i]

            if compliment in num_index:
                return [num_index[compliment], i]
            
            num_index[n] = i

        # # below is alternative algorithm to win in memory
        # for index, n in enumerate(nums):
        #     if target - n in nums[index+1:]:
        #         return [index, nums[index+1:].index(target-n)+1+index]
            