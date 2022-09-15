# 114. Flatten Binary Tree to Linked List
#
# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return root
        res = None

        def dfs(node):
            nonlocal res
            if node is None:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = res
            node.left = None
            res = node

        dfs(root)



