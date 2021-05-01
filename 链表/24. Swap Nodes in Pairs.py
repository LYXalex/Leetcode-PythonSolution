# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        first = head
        if not first or not first.next:
            return head
        second = first.next

        while first and second:
            first.val, second.val = second.val, first.val
            if second.next:
                first = first.next.next
                second = second.next.next
            else:
                second = second.next
        return head
