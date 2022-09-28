# 111. Minimum Depth of Binary Tree
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# https: // leetcode.com / problems / minimum - depth - of - binary - tree /

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], cnt: int, minTmp: int) -> int:
            if cnt == 0 and root is None:
                return 0
            cnt += 1

            if root.right is None and root.left is None:
                if cnt < minTmp:
                    minTmp = cnt

            if root.left is not None:
                minTmp = dfs(root.left, cnt, minTmp)
            if root.right is not None:
                minTmp = dfs(root.right, cnt, minTmp)
            return minTmp

        return dfs(root, 0, 10000)