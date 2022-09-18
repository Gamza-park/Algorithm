# 55. Jump Game
#
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        idx = 0
        maxVal = nums[0]

        while idx < length:
            x = nums[idx]
            print(idx, maxVal)
            if idx > maxVal:
                return False

            maxVal = max(maxVal, idx + x)
            idx += 1

        return True
