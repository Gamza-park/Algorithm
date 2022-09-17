# 66. Plus One
#
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.
#
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = 1
        cnt = 1
        res = []
        for val in reversed(digits):
            value += val * cnt
            cnt *= 10
        while cnt != 0:
            res.append(value // cnt)
            value %= cnt
            cnt //= 10
        if res[0] == 0:
            res.remove(0)
        return res