# 451. Sort Characters By Frequency
#
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
#
# Return the sorted string. If there are multiple answers, return any of them.
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/

# Big-O O(nLog(n))
class Solution:
    def frequencySort(self, s: str) -> str:
        tmp = {}
        keys = []
        for val in s:
            if val not in tmp:
                tmp[val] = 1
                keys.append(val)
            else:
                tmp[val] += 1

        sorted_by_value = sorted(keys, key=lambda x: tmp[x], reverse=True)

        res = ""

        for i in range(len(sorted_by_value)):
            res += sorted_by_value[i] * tmp[sorted_by_value[i]]

        return res


