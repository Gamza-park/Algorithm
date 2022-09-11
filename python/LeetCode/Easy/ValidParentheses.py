# 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
# 3.Every close bracket has a corresponding open bracket of the same type.

# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        tmpArr = [0, 0, 0]
        for val in s:
            type, res = self.changeInt(val)
            if tmpArr[0] >= 0 and tmpArr[1] >= 0 and tmpArr[2] >= 0:
                tmpArr[type] += res
            else:
                return False
        if tmpArr[0] == 0 and tmpArr[1] == 0 and tmpArr[2] == 0:
            if self.checkOrder(s):
                return True
            else:
                return False
        else:
            return False

    def checkOrder(self, s: str) -> bool:
        li = list(s)
        tmp = []
        while len(li) > 0:
            type, res = self.changeInt(li.pop())
            if res == -1:
                tmp.append(type)
            else:
                if tmp.pop() != type:
                    return False
        return True

    def changeInt(self, c: chr):
        type = 0;
        res = 0
        if c == "[" or c == "]":
            type = 0
            if c == "[":
                res = 1
            else:
                res = -1
        elif c == "(" or c == ")":
            type = 1
            if c == "(":
                res = 1
            else:
                res = -1
        else:
            type = 2
            if c == "{":
                res = 1
            else:
                res = -1

        return type, res