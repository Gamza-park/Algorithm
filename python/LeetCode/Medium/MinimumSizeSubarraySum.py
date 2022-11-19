# 209. Minimum Size Subarray Sum
#
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = nums[0]
        minSize = sys.maxsize
        i, j = 0, 0

        while j < len(nums) and i < len(nums):
            if sum < target:
                j = j + 1
                if j == len(nums):
                    break
                sum += nums[j]
            elif sum >= target:
                if j - i + 1 < minSize:
                    minSize=j-i+1
                sum = sum - nums[i]
                i += 1
        return 0 if minSize== sys.maxsize else minSize