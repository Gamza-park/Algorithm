# 96. Unique Binary Search Trees
#
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
# https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution:
    def numTrees(self, n: int) -> int:
        tmp = {0: 1, 1: 1}
        for i in range(2, n+1):
            m, j = 0, 0
            while j <= i-j-1:
                l = tmp[j]
                r = tmp[i-j-1]
                p = l*r
                if j != i-j-1:
                    p *= 2
                m += p
                j += 1
            tmp[i] = m
        return tmp[n]
