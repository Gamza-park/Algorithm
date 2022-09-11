# 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        tmp1 = self.makeList(l1, [])
        tmp2 = self.makeList(l2, [])

        res = self.makeInt(tmp1) + self.makeInt(tmp2)
        return self.makeListNode(res, [])

    def makeList(self, li: Optional[ListNode], res) -> List:
        tmp = li
        while tmp:
            res.append(tmp.val)
            tmp = tmp.next
        return res

    def makeInt(self, li) -> int:
        res = 0
        cnt = 1
        for i in li:
            res += i * cnt
            cnt *= 10

        return res

    def makeListNode(self, num: int, li) -> Optional[ListNode]:
        if num == 0:
            return ListNode()
        tmp = num

        while tmp > 0:
            li.append(tmp % 10)
            tmp //= 10

        head = None
        for i in reversed(li):
            head = ListNode(i, next=head)

        return head
