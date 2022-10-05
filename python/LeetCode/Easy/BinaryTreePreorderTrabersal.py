# 144. Binary Tree Preorder Traversal
#
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root: Optional[TreeNode], li: List[int]) -> List[int]:
            if not root:
                return li

            li.append(root.val)
            if root.left is not None:
                li = dfs(root.left, li)
            if root.right is not None:
                li = dfs(root.right, li)

            return li

        return dfs(root, [])