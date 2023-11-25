# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tmpList = []

        def dfs(node, depth):
            if node == None:
                return

            depth += 1

            if len(tmpList) < depth:
                tmpList.append([])

            tmpList[depth - 1].append(node.val)

            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)

        result = []

        for idx in range(len(tmpList)):
            if idx % 2 == 0:
                result.append(tmpList[idx])
            else:
                result.append(reversed(tmpList[idx]))

        return result
