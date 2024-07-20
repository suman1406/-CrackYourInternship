# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum % k == 0:
                    count+=1

        return count