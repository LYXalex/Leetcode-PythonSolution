# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        self.val = root.val

        def same(cur):
            if not cur:
                return True

            return cur.val == self.val and same(cur.left) and same(cur.right)

        return same(root)
