# 101. Symmetric Tree
#
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def dfs_l(root: Optional[TreeNode], res) -> Optional[TreeNode]:
            if root is None:
                res.append(None)
                return res

            res.append(root.val)
            dfs_l(root.left, res)
            dfs_l(root.right, res)

            return res

        def dfs_r(root: Optional[TreeNode], res) -> Optional[TreeNode]:
            if root is None:
                res.append(None)
                return res

            res.append(root.val)
            dfs_r(root.right, res)
            dfs_r(root.left, res)

            return res

        return dfs_l(root.left, []) == dfs_r(root.right, [])
