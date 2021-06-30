# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        dummy = head
        addIn = 0
        #         while l1 or l2:
        #             if not l1:
        #                 sum = (addIn + l2.val) % 10
        #                 addIn = (addIn + l2.val) // 10
        #                 l2 = l2.next
        #             elif not l2:
        #                 sum = (addIn + l1.val) % 10
        #                 addIn = (addIn + l1.val) // 10
        #                 l1 = l1.next
        #             else:
        #                 sum =  (addIn + l2.val+l1.val) % 10
        #                 addIn = (addIn + l2.val+l1.val) // 10
        #                 l1 = l1.next
        #                 l2 = l2.next

        #             head.next = ListNode(sum)
        #             head = head.next
        while l1 or l2:
            if l1:
                addIn += l1.val
                l1 = l1.next
            if l2:
                addIn += l2.val
                l2 = l2.next
            head.next = ListNode(addIn % 10)
            addIn = addIn // 10
            head = head.next
        if addIn:
            head.next = ListNode(addIn)
            head = head.next

        return dummy.next