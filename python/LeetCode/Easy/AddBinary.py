# 67. Add Binary
#
# Given two binary strings a and b, return their sum as a binary string.
#
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        value = self.changeBinaryToDecimal(a) + self.changeBinaryToDecimal(b)
        res = self.changeDecimalToBinary(value)
        return res


    def changeBinaryToDecimal(self, a: str) -> int:
        res = 0
        cnt = 1
        for val in reversed(a):
            res += int(val) * cnt
            cnt *= 2
        return res

    def changeDecimalToBinary(self, a: int) -> str:
        if a == 0:
            return "0"
        cnt = 0
        res = ""
        while a != 0:
            res += str(a % 2)
            a //= 2
            cnt += 1
        return res[::-1]