# 13. Roman to Integer
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        cnt = 0
        for i in range(len(s)):
            if cnt != 0:
                cnt -= 1
                continue
            if i != len(s) - 1:
                if self.changeValue(s[i]) >= self.changeValue(s[i + 1]):
                    res += self.changeValue(s[i])
                else:
                    res += (self.changeValue(s[i + 1]) - self.changeValue(s[i]))
                    cnt += 1
            else:
                # Last
                res += self.changeValue(s[i])
        return res

    def changeValue(self, c: chr) -> int:
        res = 0
        if c == "I":
            res = 1
        elif c == "V":
            res = 5
        elif c == "X":
            res = 10
        elif c == "L":
            res = 50
        elif c == "C":
            res = 100
        elif c == "D":
            res = 500
        elif c == "M":
            res = 1000
        else:
            res = 0

        return res