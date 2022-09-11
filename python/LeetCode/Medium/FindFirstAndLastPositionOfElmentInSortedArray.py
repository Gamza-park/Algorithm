# 34. Find First and Last Position of Element in Sorted Array
#
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        isHaveRes = True
        res = []

        if len(nums) == 0:
            isHaveRes = False
        elif len(nums) == 1:
            if nums[0] == target:
                res = [0, 0]
            else:
                isHaveRes = False
        else:
            tmpList = nums
            midIdx = len(tmpList) // 2
            idxTmp = midIdx

            while True:
                if len(tmpList) == 0:
                    isHaveRes = False
                    break
                if tmpList[midIdx] is target:
                    # First check index
                    res = self.checkIdx(nums, idxTmp)
                    break

                leftList = tmpList[0:midIdx]
                rightList = tmpList[midIdx + 1:len(tmpList)]

                if tmpList[midIdx] > target:
                    # Left
                    tmpList = leftList
                    midIdx = len(leftList) // 2
                    idxTmp -= len(leftList[midIdx:])

                elif tmpList[midIdx] < target:
                    # right
                    tmpList = rightList
                    midIdx = len(rightList) // 2
                    idxTmp += len(rightList[0:midIdx + 1])

        if not isHaveRes:
            res = [-1, -1]

        return res

    def checkIdx(self, li: List[int], idx: int) -> List[int]:
        # Left Check
        leftIdx = idx
        while leftIdx >= 0:
            if li[idx] == li[leftIdx - 1] and leftIdx > 0:
                leftIdx -= 1
            else:
                break
        # Right Check
        rightIdx = idx
        while rightIdx < len(li):
            if len(li) - 1 == rightIdx:
                break
            if li[idx] == li[rightIdx + 1]:
                rightIdx += 1
            else:
                break

        return [leftIdx, rightIdx]

