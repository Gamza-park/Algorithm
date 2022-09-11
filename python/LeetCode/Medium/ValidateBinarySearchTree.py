# 98. Validate Binary Search Tree
#
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkIfValid(root, -2 ** 32, 2 ** 32)

    def checkIfValid(self, root, minRange, maxRange):
        if not root:
            return True
        if minRange >= root.val or maxRange <= root.val:
            return False
        return self.checkIfValid(root.left, minRange, root.val) and self.checkIfValid(root.right, root.val, maxRange)





