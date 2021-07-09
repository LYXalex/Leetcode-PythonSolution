# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = ListNode(-1)
        cur = head
        while cur:
            if cur.val != prev.val:
                prev = cur
                cur = cur.next
            else:
                prev.next = cur.next
                cur = prev.next
        return head

