# 145. Binary Tree Postorder Traversal
#
# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dsf(root, li) -> List[int]:
            if not root:
                return li

            if root.left is not None:
                li = dsf(root.left, li)
            if root.right is not None:
                li = dsf(root.right, li)
            li.append(root.val)

            return li

        return dsf(root, [])