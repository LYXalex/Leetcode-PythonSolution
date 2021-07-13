# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth1(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)

        def dfs(cur):
            if not cur: return 0
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        return dfs(root)

    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left: return right + 1
        if not right: return left + 1
        return 1 + min(left, right)