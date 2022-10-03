# 162. Find Peak Element
#
# A peak element is an element that is strictly greater than its neighbors.
#
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
#
# https://leetcode.com/problems/find-peak-element/description/

# This is O(n)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxIdx = 0

        if len(nums) == 1:
            return maxIdx

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                maxIdx = i

        return maxIdx

# This is O(log n)
class Solution:
    def findPeakElement(nums: List[int]) -> int:
        res = 0

        centerIdx = len(nums) // 2

        if len(nums) == 1:
            return res
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        endIdx = len(nums) - 1
        while True:
            if centerIdx == endIdx or centerIdx == 0 \
                or (nums[centerIdx] > nums[centerIdx+1] and nums[centerIdx - 1] < nums[centerIdx]):
                # Peak
                res = centerIdx
                break
            elif nums[centerIdx] < nums[centerIdx - 1]:
                centerIdx -= 1
            elif nums[centerIdx] < nums[centerIdx + 1]:
                centerIdx += 1

        return res