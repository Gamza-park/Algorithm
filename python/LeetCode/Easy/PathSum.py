# 112. Path Sum
#
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
# https: // leetcode.com / problems / path - sum /

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root: Optional[TreeNode], sumTmp: int):
            if root is None:
                return
            sumTmp += root.val
            if not root.left and not root.right:
                return sumTmp == targetSum
            return dfs(root.left, sumTmp) or dfs(root.right, sumTmp)

        return dfs(root, 0)