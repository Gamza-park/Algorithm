# 5. Longest Palindromic Substring
#
# Given a string s, return the longest palindromic substring in s.
#
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def check(s, x, y):
            while x>= 0 and y < len(s) and s[x] == s[y]:
                x -= 1
                y += 1
            return s[x + 1: y]

        for i in range(len(s)):
            tmp1 = check(s, i, i)
            if len(res) < len(tmp1):
                res = tmp1
            tmp2 = check(s, i, i+1)
            if len(res) < len(tmp2):
                res = tmp2
        return res