# 171. Excel Sheet Column Number
#
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
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
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        idx = 1
        for val in reversed(columnTitle):
            res += (ord(val) - 64) * idx
            idx *= 26

        return res
