# 29. Divide Two Integers
#
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
#
# https: // leetcode.com / problems / divide - two - integers /

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isMinus = self.checkMinus(dividend, divisor)

        absDividend, absDivisor = abs(dividend), abs(divisor)

        if absDivisor == 1:
            quotient = absDividend
        else:
            # 계산 처리
            quotient = 0
            while absDividend >= absDivisor:
                tmp, i = absDivisor, 1
                while absDividend >= tmp:
                    absDividend -= tmp
                    quotient += i
                    i *= 2
                    tmp *= 2

        if isMinus:
            return max(-2 ** 31, -quotient)
        else:
            return min(2 ** 31 - 1, quotient)

    def checkMinus(self, x, y) -> bool:
        minusFlag = 0
        if x < 0:
            minusFlag += 1
        if y < 0:
            minusFlag += 1

        if minusFlag == 1:
            return True
        else:
            return False
