# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        traverse1, traverse2 = [], []

        def dfs(cur, leaf):
            if not cur:
                return

            if not cur.left and not cur.right:
                leaf.append(cur.val)

            if cur.left:
                dfs(cur.left, leaf)
            if cur.right:
                dfs(cur.right, leaf)

        dfs(root1, traverse1)
        dfs(root2, traverse2)

        return traverse1 == traverse2
