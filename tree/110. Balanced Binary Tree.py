# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ## worst case O(nlogn)
    def isBalanced1(self, root: TreeNode) -> bool:

        def height(cur):
            if not cur:
                return 0
            left = height(cur.left)
            right = height(cur.right)
            return max(left, right) + 1

        if not root:
            return True

        leftH = height(root.left)
        leftR = height(root.right)

        return abs(leftH - leftR) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    ## optimized O(n)
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True

        def height(cur):
            if not cur or not self.balanced:
                return 0
            left = height(cur.left)
            right = height(cur.right)
            if abs(left - right) > 1:
                self.balanced = False
                return 0
            return max(left, right) + 1

        height(root)
        return self.balanced