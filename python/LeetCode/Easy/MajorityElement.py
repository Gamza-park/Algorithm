# 169. Majority Element
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        tmp = len(nums)//2
        for val in nums:
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1
            if dic[val] > tmp:
                return val