# 33. Search in Rotated Sorted Array
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# https://leetcode.com/submissions/detail/762807229/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        tmpList = nums

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return result

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return result

        midIdx = len(nums) // 2
        idxTmp = midIdx
        while True:
            if nums[idxTmp] == target:
                result = idxTmp
                break
            leftList = tmpList[0:midIdx]
            rightList = tmpList[midIdx + 1:len(tmpList)]

            if midIdx == 0:
                break

            isValueInLeftArray = self.checkLeftRightArraySorted(leftList, rightList, target)

            if isValueInLeftArray:
                # LeftArray
                midIdx = len(leftList) // 2
                idxTmp -= len(leftList[midIdx:])
                tmpList = leftList
            else:
                # Right Array
                midIdx = len(rightList) // 2
                idxTmp += len(rightList[0:midIdx + 1])
                tmpList = rightList

        return result

    def checkLeftRightArraySorted(self, leftLi: List[int], rightLi: List[int], x: int) -> bool:
        # True is Left Array, False is Right Array

        isLeftLiSorted = self.checkSortedArray(leftLi)

        if isLeftLiSorted:
            if x >= leftLi[0] and x <= leftLi[len(leftLi) - 1]:
                return True
            else:
                return False
        else:
            if len(rightLi) is 0:
                return True
            else:
                if x >= rightLi[0] and x <= rightLi[len(rightLi) - 1]:
                    return False
                else:
                    return True

    def checkSortedArray(self, li: List[int]) -> bool:
        if li[0] < li[-1]:
            return True
        else:
            return False
