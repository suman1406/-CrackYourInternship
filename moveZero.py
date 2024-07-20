# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos] = nums[i]
                non_zero_pos+=1

        for i in range(non_zero_pos, len(nums)):
            nums[i] = 0