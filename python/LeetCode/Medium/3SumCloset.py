# 16. 3Sum Closest
#
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minTmp = 10001
        res = 0
        for i in range(len(nums) - 2):

            j, r = i + 1, len(nums) - 1

            while j < r:
                sumTmp = nums[i] + nums[j] + nums[r]

                if sumTmp < target:
                    j += 1
                else:
                    r -= 1
                diff = abs(target - sumTmp)
                if diff < minTmp:
                    minTmp = diff
                    res = sumTmp

        return res
