# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], cnt: int):
            if node == None:
                return cnt

            cnt += 1

            if node.left != None:
                cnt = dfs(node.left, cnt)
            if node.right != None:
                cnt = dfs(node.right, cnt)

            return cnt

        res = dfs(root, 0)

        return res
