# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reverse(head):
            prev, cur = None, head
            while cur:
                cur.next, prev, cur = prev, cur, cur.next
            return prev

        reverse1 = reverse(l1)
        reverse2 = reverse(l2)
        carrier, ans = 0, ListNode(0)
        temp = ans
        while reverse1 or reverse2:
            temp1 = reverse1.val if reverse1 else 0
            temp2 = reverse2.val if reverse2 else 0
            sumV = temp1 + temp2 + carrier
            carrier = sumV // 10
            temp.next = ListNode(sumV % 10)
            if reverse1: reverse1 = reverse1.next
            if reverse2: reverse2 = reverse2.next
            temp = temp.next
        if carrier != 0:
            temp.next = ListNode(carrier)
        return reverse(ans.next)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        sumV = str(num1 + num2)

        i, ans = 0, ListNode(0)
        temp = ans
        while i < len(sumV):
            temp.next = ListNode(int(sumV[i:i + 1]))
            temp = temp.next
            i += 1
        return ans.next





