# 74. Search a 2D Matrix
#
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        midIdx = len(matrix) // 2
        tmpMatrix = matrix
        dontHaveValue = False

        while True:
            if tmpMatrix:
                listFlag = self.checkInToMatrix(tmpMatrix[midIdx], target)
            else:
                # Range of matrix
                dontHaveValue = True
                break

            leftMatrix = tmpMatrix[:midIdx]
            rightMatrix = tmpMatrix[midIdx+1:]

            if listFlag == 0:
                # left
                midIdx = len(leftMatrix) // 2
                tmpMatrix = leftMatrix
            elif listFlag == 1:
                # inside
                tmpMatrix = tmpMatrix[midIdx]
                break
            else:
                # right
                midIdx = len(rightMatrix) // 2
                tmpMatrix = rightMatrix


        if dontHaveValue:
            return False

        return self.checkInToList(tmpMatrix, target)



    def checkInToMatrix(self, list: List[int], target) -> int:
        if target < list[0]:
            # left
            return 0
        elif target > list[len(list) - 1]:
            # right
            return 2
        else:
            # into
            return 1

    def checkInToList(self, list: List[int], target) -> bool:

        tmpList = list
        midIdx = len(tmpList) // 2

        while tmpList:

            if tmpList[midIdx] == target:
                return True

            leftList = tmpList[:midIdx]
            rightList = tmpList[midIdx+1:]

            if tmpList[midIdx] > target:
                # left
                midIdx = len(leftList) // 2
                tmpList = leftList
            else:
                # right
                midIdx = len(rightList) // 2
                tmpList = rightList

        return False






