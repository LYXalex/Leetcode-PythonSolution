# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        cur, num = head, 0
        while cur:
            num += 1
            cur = cur.next

        def dfs(head, length):
            if not head or not length: return None
            cur = head
            mid = (length + 1) >> 1
            while mid > 1:
                mid -= 1
                cur = cur.next
            root = TreeNode(cur.val)
            mid = (length + 1) >> 1
            root.left = dfs(head, mid - 1)
            root.right = dfs(cur.next, length - mid)
            return root

        return dfs(head, num)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        if not head.next: return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)
        return root

