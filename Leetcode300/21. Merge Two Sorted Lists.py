# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp = ListNode(0)
        dummy = temp
        while l1 or l2:
            if not l1:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        return dummy.next