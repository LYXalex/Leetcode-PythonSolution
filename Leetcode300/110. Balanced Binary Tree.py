# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced1(self, root: TreeNode) -> bool:
        def dfs(cur):
            if not cur: return 0
            l = dfs(cur.left)
            if l == -1: return -1
            r = dfs(cur.right)
            if r == -1: return -1
            if abs(l - r) > 1: return -1
            return max(l, r) + 1

        return dfs(root) != -1

    def isBalanced(self, root: TreeNode) -> bool:
        def height(cur):
            if not cur: return 0
            return 1 + max(height(cur.left), height(cur.right))

        if not root: return True
        l = height(root.left)
        r = height(root.right)
        return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
