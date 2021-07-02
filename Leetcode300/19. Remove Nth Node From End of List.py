# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        num = 0
        while cur:
            cur = cur.next
            num += 1
        if n == num:
            head = head.next
            return head

        cur = head
        index = 0
        while cur:
            if index == num - n - 1:
                next = cur.next.next
                cur.next = next
                break
            cur = cur.next
            index += 1
        return head


