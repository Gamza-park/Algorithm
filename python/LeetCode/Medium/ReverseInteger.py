# 7. Reverse Integer
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        resTmp = ""
        if x >= 0:
            tmp = x
            while True:
                resTmp += str(tmp % 10)
                tmp = tmp // 10
                if tmp == 0:
                    break
            res = int(resTmp)
            if res < -2 ** 31 or res > 2 ** 31 - 1:
                return 0
        else:
            tmp = x * -1
            while True:
                resTmp += str(tmp % 10)
                tmp = tmp // 10
                if tmp == 0:
                    break
            res = int(resTmp) * -1
            if res < -2 ** 31 or res > 2 ** 31 - 1:
                return 0

        return res