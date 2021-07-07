# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k: return head
        cur, len = head, 0
        while cur:
            if cur: tail = cur
            cur = cur.next
            len += 1

        num = len - k % len
        if num == len: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while num:
            num -= 1
            cur = cur.next

        tail.next = dummy.next
        dummy.next = cur.next
        cur.next = None
        return dummy.next


