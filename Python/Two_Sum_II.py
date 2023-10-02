"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:


        forwards, backwards = 0, len(numbers)-1
        while forwards < backwards:

            # skip if previous element was identical
            if forwards > 0 and numbers[forwards] == numbers[forwards-1]:
                forwards+=1
                continue
            elif backwards < len(numbers)-1 and numbers[backwards] == numbers[backwards+1]:
                backwards-=1
                continue

            if numbers[forwards] + numbers[backwards] > target:
                backwards-=1
            elif numbers[forwards] + numbers[backwards] < target:
                forwards+=1
            else:
                return [forwards+1, backwards+1]