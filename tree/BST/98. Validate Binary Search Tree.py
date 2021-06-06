# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    import math
    def isValidBST1(self, root: TreeNode) -> bool:
        self.prev = -math.inf

        def inorderTraversal(root):
            if not root: return True
            left = inorderTraversal(root.left)
            if not left: return False
            if root.val <= self.prev: return False
            self.prev = root.val
            return inorderTraversal(root.right)

        return inorderTraversal(root)

    # iterative
    def isValidBST(self, root: TreeNode) -> bool:
        stack = deque()
        prev = -math.inf
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev: return False
            prev = root.val
            root = root.right
        return True