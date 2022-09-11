# 61. Rotate List
#
# Given the head of a linked list, rotate the list to the right by k places.
#
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, last = ListNode(0, head), ListNode(0, head)
        nodeForCnt = head
        length = 0

        # check Length
        while nodeForCnt:
            length += 1
            nodeForCnt = nodeForCnt.next

        if length == 0 or length == 1 or k == 0 or k % length == 0:
            return head

        # Check move List Cnt
        k = k % length

        while k >= 0:
            k -= 1
            first = first.next

        end = ListNode()

        while first:
            if first.next == None:
                end = first
            first = first.next
            last = last.next

        newHead = last.next
        last.next = None
        end.next = head

        return newHead

