# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        self.ans = 0

        def helper(node):
            if not node:
                return 'covered'
            l = helper(node.left)
            r = helper(node.right)
            if l == r == 'covered':
                return 'leaf'
            if l == 'leaf' or r == 'leaf':
                self.ans += 1
                return 'camera'
            if l == 'camera' or r == 'camera':
                return 'covered'

        return ((helper(root) == 'leaf') + self.ans)


