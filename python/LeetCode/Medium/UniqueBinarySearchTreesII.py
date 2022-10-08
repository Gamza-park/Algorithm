# 95. Unique Binary Search Trees II
#
# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dp(i, j):
            if i > j: return [None]
            res = []

            for k in range(i, j + 1):
                for lft, rgh in product(dp(i, k - 1), dp(k + 1, j)):
                    root = ListNode(k)
                    root.left = lft
                    root.right = rgh
                    res.append(root)
            return res

        return dp(1, n)