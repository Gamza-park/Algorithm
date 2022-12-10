# 1339. Maximum Product of Splitted Binary Tree
#
# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
#
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
#
# Note that you need to maximize the answer before taking the mod and not after taking it.
#
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        global maxValue
        maxValue = 0

        def dfs(node, sum):
            sum += node.val

            if node.left:
                sum = dfs(node.left, sum)

            if node.right:
                sum = dfs(node.right, sum)

            return sum

        totalSum = dfs(root, 0)

        def second_dfs(node):
            global maxValue

            curValue = node.val
            if node.left:
                curValue += second_dfs(node.left)
            if node.right:
                curValue += second_dfs(node.right)

            minusVal = totalSum - curValue
            if maxValue < curValue * minusVal:
                maxValue = curValue * minusVal
            return curValue

        second_dfs(root)

        maxValue %= 10 ** 9 + 7

        return maxValue
