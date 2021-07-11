# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    # iterative
    def recoverTree1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        stack = []
        prev = ListNode(-math.inf)
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val < prev.val:
                if not first: first = prev
                second = root
            prev = root
            root = root.right
        first.val, second.val = second.val, first.val

    # recursion
    def recoverTree(self, root: TreeNode) -> None:
        self.first = None
        self.second = None
        self.prev = ListNode(-math.inf)

        def inorderTraversal(cur):
            if not cur: return
            inorderTraversal(cur.left)
            if cur.val <= self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = cur
            self.prev = cur
            inorderTraversal(cur.right)

        inorderTraversal(root)
        self.first.val, self.second.val = self.second.val, self.first.val







