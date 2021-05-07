# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0)

        while head:
            if curr and head.val < curr.val:
                curr = dummy
            while curr.next and head.val > curr.next.val:
                curr = curr.next

            # curr.next,curr.next.next,head = head,curr.next,head.next
            next = curr.next
            temp = head.next
            curr.next = head
            curr.next.next = next
            head = temp

        return dummy.next

#     cur = dummy = ListNode(0)
#     while head:
#         if cur and cur.val > head.val: # reset pointer only when new number is smaller than pointer value
#             cur = dummy
#         while cur.next and cur.next.val < head.val: # classic insertion sort to find position
#             cur = cur.next
#         cur.next, cur.next.next, head = head, cur.next, head.next # insert
#     return dummy.next