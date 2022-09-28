# 110. Balanced Binary Tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(root: Optional[TreeNode], cnt: int, maxTmp: int) -> int:
            if root is None:
                return maxTmp
            cnt += 1
            if root.left is None and root.left is None:
                if maxTmp < cnt:
                    maxTmp = cnt
            maxTmp = dfs(root.left, cnt, maxTmp)
            maxTmp = dfs(root.right, cnt, maxTmp)

            return maxTmp

        return abs(dfs(root.left, 0, 0) - dfs(root.right, 0, 0)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

