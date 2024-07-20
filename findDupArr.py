# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        
        return dup