# 94. Binary Tree Inorder Traversal
#
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        def dfs(root,res):
            if root is None: return
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right,res)
            return res
        return dfs(root,[])