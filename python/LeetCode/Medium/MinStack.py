# 155. Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
#
# https: // leetcode.com / problems / min - stack /

class MinStack:

    def __init__(self):
        self.__stack = []
        self.__stack_m = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        m = self.__stack_m
        if not m:
            m.append(val)
        else:
            m.append(min(val, m[-1]))

    def pop(self) -> None:
        self.__stack.pop()
        self.__stack_m.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__stack_m[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()