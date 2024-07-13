# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
# Solved
# Medium
# Topics
# Companies
# Hint
# A critical point in a linked list is defined as either a local maxima or a local minima.

# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2024-07-05

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = self.dfs(head, 1, [], None)

        if len(arr) < 2:
            return [-1, -1]

        min = inf
        for idx in range(len(arr) - 1):
            if arr[idx + 1] - arr[idx] < min:
                min = arr[idx + 1] - arr[idx]

        return [
            min,
            arr[len(arr) - 1] - arr[0]
        ]
    


    def dfs(self, head, idx, arr, currentVal = None):
        if head.next:
            if currentVal:
                val = head.val
                nextVal = head.next.val
                if currentVal > val and val < nextVal:
                    arr.append(idx)
                elif currentVal < val and val > nextVal:
                    arr.append(idx)
            arr = self.dfs(head.next, idx+1, arr, head.val)
        
        return arr
