# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # iterative
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head
        num = 0
        while prev and cur:
            num += 1
            if num == left:
                left_head = prev
                start = cur

            while num >= left and num <= right:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                num += 1

                if num == right + 1:
                    left_head.next = prev
                    start.next = cur

            if num >= right: break

            prev = cur
            cur = cur.next

        return dummy.next

