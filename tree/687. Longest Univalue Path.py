# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath1(self, root: TreeNode) -> int:

        self.ans = 1

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            if not (node.left and node.val == node.left.val): left = 0

            if not (node.right and node.val == node.right.val): right = 0

            self.ans = max(self.ans, left + right + 1)

            return 1 + max(left, right)

        helper(root)
        return self.ans - 1

    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.ans = 0

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            left = left + 1 if node.left and node.val == node.left.val else 0
            right = right + 1 if node.right and node.val == node.right.val else 0

            self.ans = max(self.ans, left + right)

            return max(left, right)

        helper(root)
        return self.ans
