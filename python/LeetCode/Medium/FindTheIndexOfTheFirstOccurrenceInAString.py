# 28. Find the Index of the First Occurrence in a String
#
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)