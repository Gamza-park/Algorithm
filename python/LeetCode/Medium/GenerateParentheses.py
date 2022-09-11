# 22. Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTracking(first, second):
            if first == second == n:
                res.append(self.makeString(stack))
                return

            if first < n:
                stack.append("(")
                backTracking(first + 1, second)
                stack.pop()

            if second < first:
                stack.append(")")
                backTracking(first, second + 1)
                stack.pop()

        backTracking(0, 0)

        return res

    def makeString(self, li):
        res = ""
        for i in li:
            res += i
        return res
