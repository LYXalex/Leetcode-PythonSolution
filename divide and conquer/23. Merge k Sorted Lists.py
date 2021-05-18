# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# import heapq
class Solution:

    # priority queue
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        h = []
        curr = dummy = ListNode(0)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        return dummy.next

    # divide and concquer
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l, r):
            newList = dummy = ListNode(0)
            while l and r:
                if l.val < r.val:
                    newList.next = ListNode(l.val)
                    l = l.next
                else:
                    newList.next = ListNode(r.val)
                    r = r.next
                newList = newList.next
            if l or r:
                newList.next = l or r
            return dummy.next

        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        end, start = 0, len(lists)
        mid = start + (end - start) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return merge(l, r)








