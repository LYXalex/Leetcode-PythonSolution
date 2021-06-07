# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    def recoverTree1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.prev = TreeNode(-math.inf)

        def inorderTraversal(root):
            if not root: return
            inorderTraversal(root.left)
            if root.val <= self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = root
            self.prev = root
            inorderTraversal(root.right)

        if not root: return
        self.first = None
        self.second = None
        inorderTraversal(root)
        if self.first and self.second:
            temp = self.first.val
            self.first.val = self.second.val
            self.second.val = temp
        return root

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        sec = None
        prev = TreeNode(-math.inf)

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev.val:
                if not first: first = prev
                second = root
            prev = root
            root = root.right
        first.val, second.val = second.val, first.val
        return root




