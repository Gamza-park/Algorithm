# 6. Zigzag Conversion
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        for i in range(1, numRows + 1):
            if i == 1 or i == numRows:
                tmp = i - 1
                while len(s) > tmp:
                    res += s[tmp]
                    tmp += numRows + (numRows - 2)

            else:
                tmp = i - 1
                flag = (numRows - 2) - (tmp - 1)
                x = (numRows - 1) - flag
                checkFlag = True
                while len(s) > tmp:
                    res += s[tmp]
                    if checkFlag:
                        tmp += flag * 2
                        checkFlag = False
                    else:
                        tmp += x * 2
                        checkFlag = True

        return res
