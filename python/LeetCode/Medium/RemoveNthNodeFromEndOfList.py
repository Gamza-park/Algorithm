# 19. Remove Nth Node From End of List
#
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return

        valList = []
        cur = head
        while cur:
            valList.append(cur.val)
            cur = cur.next

        valList.pop(len(valList) - n)

        res = ListNode()
        isFirst = True
        for val in reversed(valList):
            tmpNode = ListNode(val, None)
            if isFirst:
                res = tmpNode
                isFirst = False
                continue
            tmpNode = ListNode(val, None)
            tmpNode.next = res
            res = tmpNode

        return res
