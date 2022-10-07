# 168. Excel Sheet Column Title
#
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber < 27:
            return chr(columnNumber + 64)

        tmp = []

        while True:
            if columnNumber % 26 == 0:
                tmpVal = 26
                columnNumber -= 1
            else:
                tmpVal = columnNumber % 26

            tmp.insert(0, tmpVal)
            columnNumber //= 26

            if columnNumber <= 26:
                tmp.insert(0, columnNumber)
                break

        return self.listToExcel(tmp, "")

    def listToExcel(self, list: List, res: str) -> str:
        for val in list:
            res += chr(val + 64)

        return res