# 113. Path Sum II
#
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
#
# https: // leetcode.com / problems / path - sum - ii /

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        targetSumTmp = targetSum - root.val

        if root.left is None and root.right is None:
            if targetSumTmp == 0:
                return [[root.val]]
            else:
                return []

        res = []

        def dfs(node, target, li):

            targetTmp = target - node.val
            tmpLi = li + [node.val]
            if node.left:
                dfs(node.left, targetTmp, tmpLi)
            if node.right:
                dfs(node.right, targetTmp, tmpLi)

            if targetTmp == 0 and node.right is None and node.left is None:
                res.append(tmpLi)

        if root.left:
            dfs(root.left, targetSumTmp, [root.val])
        if root.right:
            dfs(root.right, targetSumTmp, [root.val])

        return res

