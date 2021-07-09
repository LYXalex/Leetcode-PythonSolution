# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # iterative
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head
        cur = head
        greater = None
        # great_prev = None
        while cur:
            if cur.val < x and greater:
                prev.next = cur.next
                greater_prev.next = cur
                cur.next = greater
                greater_prev = greater_prev.next
                cur = prev.next
            elif cur.val >= x and not greater:
                greater = cur
                greater_prev = prev
                prev = cur
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return dummy.next

