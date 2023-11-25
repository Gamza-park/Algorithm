# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def checkList(li, target, hasData):
            centerIdx = len(li) // 2

            if li[centerIdx] == target:
                return True

            if len(li) == 1:
                return hasData

            if li[centerIdx] > target:
                hasData = checkList(li[:centerIdx], target, hasData)
            elif li[centerIdx] < target:
                hasData = checkList(li[centerIdx:], target, hasData)

            if hasData:
                return hasData

        for li in matrix:
            result = checkList(li, target, False)
            if result:
                return True

        return False
