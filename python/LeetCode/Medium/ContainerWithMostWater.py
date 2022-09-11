# 11. Container With Most Water
#
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_idx, r_idx = 0, len(height) - 1
        res = 0

        while l_idx < r_idx:
            tmp = (r_idx - l_idx) * min(height[l_idx], height[r_idx])

            if res < tmp:
                res = tmp

            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
        return res
