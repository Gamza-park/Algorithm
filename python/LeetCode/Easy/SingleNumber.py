# 136. Single Number
#
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# https: // leetcode.com / problems / single - number /

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]