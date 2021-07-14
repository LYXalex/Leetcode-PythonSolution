# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right
            else:
                pre = root.left
                while pre.right: pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
                root = root.right

    def flatten(self, root: TreeNode) -> None:
        self.prev = None

        def helper(root):
            if not root: return None
            helper(root.right)
            helper(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root

        helper(root)


