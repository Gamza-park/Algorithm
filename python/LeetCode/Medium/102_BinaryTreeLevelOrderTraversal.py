# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, depth):
            if node == None:
                return
            depth += 1
            if len(result) < depth:
                result.append([])
            result[depth - 1].append(node.val)

            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)

        return result