# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:

        prev = ListNode(0)
        dummy = prev
        prev.next = head
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return dummy.next

    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode(0)
        dummy = prev
        prev.next = head
        while prev.next and prev.next.next:
            x1 = prev.next
            x2 = prev.next.next
            prev.next = x2
            x1.next = x2.next
            x2.next = x1
            prev = prev.next.next
        return dummy.next



