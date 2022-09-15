# 58. Length of Last Word
#
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for val in reversed(s):
            if val != " ":
                cnt += 1
            else:
                if cnt != 0:
                    break
        return cnt
