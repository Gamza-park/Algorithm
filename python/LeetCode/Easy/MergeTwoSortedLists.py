# 21. Merge Two Sorted Lists
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 != None and list2 != None:
            # 둘다 값이 존재
            arr = []
            while list1.val != 101 or list2.val != 101:
                if list1.val <= list2.val:
                    arr.append(list1.val)
                    # 리스트1 배열 아웃풋 리스트노드에 추가.
                    if list1.next != None:
                        list1.val = list1.next.val
                        list1.next = list1.next.next
                    else:
                        list1.val = 101
                else:
                    # 리스트2 배열 아우풋 리스트노드에 추가
                    arr.append(list2.val)
                    if list2.next != None:
                        list2.val = list2.next.val
                        list2.next = list2.next.next
                    else:
                        list2.val = 101
            return self.makeNode(arr)
        else:
            # None 값이 존재
            if list1 == None:
                # list1이 None, list2출력(None이여도 None값출력)
                return list2
            else:
                # list2이 None, list1출력(None이여도 None값출력)
                return list1

    def makeNode(self, arr: int) -> Optional[ListNode]:
        tmp = ListNode()
        cnt = 0
        for va in reversed(arr):
            print("cnt is :", cnt + 1, va)
            if cnt == 0:
                tmp = ListNode(va, None)
            else:
                newNode = ListNode(va, None)
                newNode.next = tmp
                tmp = newNode
            cnt += 1

        return tmp