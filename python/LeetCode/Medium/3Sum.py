# 15. 3Sum
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, r = i + 1, n - 1

            while j < r:
                sum = nums[i] + nums[j] + nums[r]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[r]])
                    while j + 1 < r and nums[j] == nums[j + 1]:
                        j += 1
                    while r - 1 > j and nums[r] == nums[r - 1]:
                        r -= 1
                    j += 1
                    r -= 1

        return res
