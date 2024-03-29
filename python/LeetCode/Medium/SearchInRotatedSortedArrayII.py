# 81. Search in Rotated Sorted Array II
#
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
#
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
#
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
#
# You must decrease the overall operation steps as much as possible.
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            midIdx = (left + right) // 2

            if nums[midIdx] == target:
                return True

            if nums[left] < nums[midIdx]:
                if nums[left] <= target <= nums[midIdx]:
                    # sorted List
                    right = midIdx - 1
                else:
                    left = midIdx
            elif nums[left] > nums[midIdx]:
                if nums[midIdx] <= target <= nums[right]:
                    left = midIdx + 1
                else:
                    right = midIdx - 1
            else:
                left += 1

        return False
