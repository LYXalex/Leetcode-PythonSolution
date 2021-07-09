# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                prev = cur
                cur = cur.next
            else:
                cur = cur.next
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
                cur = prev.next
        return dummy.next

