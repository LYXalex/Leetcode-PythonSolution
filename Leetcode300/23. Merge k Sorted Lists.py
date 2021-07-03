# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = []
        for i in range(len(lists)):  ## 注意不要list in lists
            if lists[i]:
                heapq.heappush(queue, (lists[i].val, i))
                lists[i] = lists[i].next
        head = ListNode(0)
        dummy = head
        while queue:
            val, num = heapq.heappop(queue)
            head.next = ListNode(val)
            head = head.next
            if lists[num]:
                heapq.heappush(queue, (lists[num].val, num))
                lists[num] = lists[num].next
        return dummy.next



