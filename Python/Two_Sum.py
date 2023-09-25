
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, n in enumerate(nums):
            for i in range(index+1, len(nums)):
                if nums[index]+nums[i] == target:
                    return [index, i]
# https://leetcode.com/problems/two-sum/description/