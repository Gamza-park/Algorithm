# 9. Palindrome Number
#
# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
# For example, 121 is a palindrome while 123 is not.

# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = []
        tmp = tmp2 = x
        while True:
            a.append(tmp % 10)
            tmp = tmp // 10
            if tmp == 0:
                break
        for i in reversed(range(len(a))):
            if a[i] != tmp2 % 10:
                return False
            tmp2 = tmp2 // 10
        return True