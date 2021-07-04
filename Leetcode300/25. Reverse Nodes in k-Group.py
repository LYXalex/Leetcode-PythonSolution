# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:

        cur, num = head, 0
        while cur:
            cur = cur.next
            num += 1

        prev = ListNode(0)
        cur = head
        dummy = prev
        t = num // k
        before_interval = dummy
        for i in range(t):
            first_interval = cur
            for j in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            first_interval.next = cur
            before_interval.next = prev
            before_interval = first_interval
        return dummy.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        count, node = 0, head
        while count < k:
            count += 1
            if not node: return head
            node = node.next

        def reverse(head, count):
            prev, cur = None, head
            while count > 0:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                count -= 1
            return cur, prev

        newHead, prev = reverse(head, count)
        head.next = self.reverseKGroup(newHead, count)
        return prev














