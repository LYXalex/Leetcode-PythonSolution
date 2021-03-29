# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        def dfs(cur):
            if not cur:
                return None
            if cur.val >= low and cur.val <= high:
                cur.left = dfs(cur.left)
                cur.right = dfs(cur.right)
                return cur
            if cur.val < low:
                return dfs(cur.right)
            if cur.val > high:
                return dfs(cur.left)

        return dfs(root)



