# 45. Jump Game II
#
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    continue
                if cnt[i + j] == 0:
                    cnt[i + j] = cnt[i] + 1

        return cnt[len(nums) - 1]
