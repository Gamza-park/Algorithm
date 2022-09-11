# 24. Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        node = head
        cnt = 1
        while node:
            if cnt % 2 == 1 and node.next:
                x = node.val
                node.val = node.next.val
                node.next.val = x
            node = node.next
            cnt += 1
        return head
