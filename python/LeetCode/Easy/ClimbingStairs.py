# 70. Climbing Stairs
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3:
            return n
        # Start
        a = []
        a.insert(0, 1)
        a.insert(1, 2)
        for i in range(2, n):
            a.insert(i, a[i - 1] + a[i - 2])
        return a[n - 1]
