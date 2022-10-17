# 202. Happy Number
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = n
        while True:
            tmp = self.totalSum(tmp)
            if tmp == 1:
                return True
            if tmp == 145:
                return False



    def totalSum(self, a: int) -> int:
        res = 0
        while a != 0:
            res += (a % 10)*(a % 10)
            a //= 10

        return res