# 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        start = end = maxCnt = 0
        uniq = set()

        while end < len(s):
            if s[end] not in uniq:
                uniq.add(s[end])
                end += 1
                maxCnt = max(maxCnt, len(uniq))
            else:
                uniq.remove(s[start])
                start += 1
        return maxCnt
