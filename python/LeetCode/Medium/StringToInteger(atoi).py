# 8. String to Integer (atoi)
#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
#
# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:

        signCnt = 0
        isPositive = True
        strFlag = True
        intFlag = True
        signFlag = True

        strTmp = ""

        for i in s:
            if i == " ":
                if intFlag == False:
                    break
                if signFlag == False:
                    break
                continue
            if strFlag == False:
                break

            # 48(0) ~ 57(9)
            # 43: +,  45: -
            tmp = ord(i)

            # Check Sign(Positive, Negative)
            if tmp == 43:
                if intFlag == False:
                    break
                isPositive = True
                signCnt += 1
                signFlag = False
                if signCnt == 2:
                    break
            elif tmp == 45:
                if intFlag == False:
                    break
                isPositive = False
                signCnt += 1
                signFlag = False
                if signCnt == 2:
                    break

            # Check number
            if tmp >= 48 and tmp <= 57:
                strTmp += i
                intFlag = False
            else:
                if intFlag == False:
                    break
                if tmp != 43 and tmp != 45:
                    strFlag = False

        if strTmp == '':
            return 0
        else:
            resTmp = int(strTmp)
            if isPositive:
                if resTmp > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                else:
                    return resTmp
            else:
                if resTmp * -1 < -2 ** 31:
                    return -2 ** 31
                else:
                    return resTmp * -1
