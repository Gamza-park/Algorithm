# 118. Pascal's Triangle
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tmp = []
        for i in range(numRows):
            tmp.append([])
            for j in range(i+1):
                if i < 2 or j == 0 or j == i:
                    tmp[i].append(1)
                else:
                    tmp[i].append(tmp[i-1][j-1] + tmp[i-1][j])
        return tmp